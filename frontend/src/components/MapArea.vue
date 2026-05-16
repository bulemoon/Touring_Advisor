<template>
  <div class="map-wrapper">
    <div ref="mapContainer" class="map-area" />
    <button class="locate-btn" @click="relocate" :class="{ locating }" title="定位到当前位置">
      <span class="material-icons">my_location</span>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue"
import L from "leaflet"
import "leaflet/dist/leaflet.css"

const emit = defineEmits<{ located: [lat: number, lng: number] }>()

const mapContainer = ref<HTMLDivElement>()
let map: L.Map | null = null
let currentMarker: L.Marker | null = null
const locating = ref(false)

const DEFAULT_LAT = 39.9042
const DEFAULT_LNG = 116.4074

const locationIcon = L.icon({
  iconUrl: "/icons/location-pin.svg",
  iconSize: [36, 36],
  iconAnchor: [18, 36],
  popupAnchor: [0, -36],
})

function addLocationMarker(lat: number, lng: number, label: string) {
  if (currentMarker) map?.removeLayer(currentMarker)
  currentMarker = L.marker([lat, lng], { icon: locationIcon })
    .addTo(map!)
    .bindPopup(label)
    .openPopup()
  return currentMarker
}

function relocate() {
  if (locating.value || !map) return
  locating.value = true
  addLocationMarker(DEFAULT_LAT, DEFAULT_LNG, "定位中…")
  locateWithAmap()
}

function loadAmapScript(): Promise<void> {
  return new Promise((resolve, reject) => {
    if ((window as any).AMap) {
      resolve()
      return
    }
    const key = (window as any).CONFIG?.AMAP_JS_KEY || "a1c8ea9da092648dd830db9490db9f4f"
    if (!key) {
      reject(new Error("AMap key missing"))
      return
    }
    const script = document.createElement("script")
    script.src = `https://webapi.amap.com/maps?v=2.0&key=${key}&plugin=AMap.Geolocation`
    script.onload = () => resolve()
    script.onerror = () => reject(new Error("AMap load failed"))
    document.head.appendChild(script)
  })
}

async function fallbackToIpLocation() {
  locating.value = false
  try {
    const res = await fetch("/api/location/ip")
    const data = await res.json()
    console.log("[IP Geo] 返回:", data)
    if (data.success) {
      map?.setView([data.lat, data.lng], 11)
      addLocationMarker(data.lat, data.lng, `${data.city || "当前城市"}（IP 定位）`)
      emit("located", data.lat, data.lng)
      return
    }
  } catch (e) {
    console.warn("[IP Geo] 失败:", e)
  }
  addLocationMarker(DEFAULT_LAT, DEFAULT_LNG, "无法定位，使用默认位置")
  emit("located", DEFAULT_LAT, DEFAULT_LNG)
}

function fallbackToNativeGeo() {
  if (!navigator.geolocation) {
    fallbackToIpLocation()
    return
  }
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const [lat, lng] = wgs84ToGcj02(pos.coords.latitude, pos.coords.longitude)
      map?.setView([lat, lng], 14)
      addLocationMarker(lat, lng, `我的位置<br/>${lat.toFixed(5)}, ${lng.toFixed(5)}`)
      emit("located", lat, lng)
    },
    (err) => {
      console.warn("[Geo] 原生定位失败:", err.code, err.message)
      fallbackToIpLocation()
    },
    { timeout: 15000, enableHighAccuracy: false, maximumAge: 300000 }
  )
}

function locateWithAmap() {
  const AMap = (window as any).AMap
  const geolocation = new AMap.Geolocation({
    enableHighAccuracy: false,
    timeout: 20000,
    needAddress: false,
    GeoLocationFirst: false,
    maximumAge: 300000,
  })

  geolocation.getCurrentPosition((status: string, result: any) => {
    locating.value = false
    if (status === "complete" && result.position) {
      const lat = result.position.getLat()
      const lng = result.position.getLng()
      map?.setView([lat, lng], 14)
      addLocationMarker(lat, lng, `我的位置<br/>${lat.toFixed(5)}, ${lng.toFixed(5)}`)
      emit("located", lat, lng)
    } else {
      console.warn("[AMap] 定位失败:", result?.info, result?.message)
      // AMap 失败，降级到浏览器原生定位
      fallbackToNativeGeo()
    }
  })
}

onMounted(async () => {
  if (!mapContainer.value) return

  map = L.map(mapContainer.value, {
    zoomControl: false,
    attributionControl: false,
  }).setView([DEFAULT_LAT, DEFAULT_LNG], 13)

  L.tileLayer(
    "https://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
    { maxZoom: 18, subdomains: ["1", "2", "3", "4"] }
  ).addTo(map)

  addLocationMarker(DEFAULT_LAT, DEFAULT_LNG, "定位中…")

  try {
    await loadAmapScript()
    locateWithAmap()
  } catch {
    fallbackToIpLocation()
  }
})

onUnmounted(() => {
  map?.remove()
})

// 仅降级用：WGS-84 → GCJ-02
function wgs84ToGcj02(lat: number, lng: number): [number, number] {
  const a = 6378245.0
  const ee = 0.00669342162296594323
  const dLat = transformLat(lng - 105.0, lat - 35.0)
  const dLng = transformLng(lng - 105.0, lat - 35.0)
  const radLat = (lat / 180.0) * Math.PI
  let magic = Math.sin(radLat)
  magic = 1 - ee * magic * magic
  const sqrtMagic = Math.sqrt(magic)
  return [
    lat + (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * Math.PI),
    lng + (dLng * 180.0) / (a / sqrtMagic * Math.cos(radLat) * Math.PI),
  ]
}

function transformLat(x: number, y: number): number {
  let ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * Math.sqrt(Math.abs(x))
  ret += (20.0 * Math.sin(6.0 * x * Math.PI) + 20.0 * Math.sin(2.0 * x * Math.PI)) * 2.0 / 3.0
  ret += (20.0 * Math.sin(y * Math.PI) + 40.0 * Math.sin(y / 3.0 * Math.PI)) * 2.0 / 3.0
  ret += (160.0 * Math.sin(y / 12.0 * Math.PI) + 320 * Math.sin(y * Math.PI / 30.0)) * 2.0 / 3.0
  return ret
}

function transformLng(x: number, y: number): number {
  let ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * Math.sqrt(Math.abs(x))
  ret += (20.0 * Math.sin(6.0 * x * Math.PI) + 20.0 * Math.sin(2.0 * x * Math.PI)) * 2.0 / 3.0
  ret += (20.0 * Math.sin(x * Math.PI) + 40.0 * Math.sin(x / 3.0 * Math.PI)) * 2.0 / 3.0
  ret += (150.0 * Math.sin(x / 12.0 * Math.PI) + 300.0 * Math.sin(x / 30.0 * Math.PI)) * 2.0 / 3.0
  return ret
}
</script>

<style scoped>
.map-wrapper {
  position: relative;
  width: 100%;
}

.map-area {
  width: 100%;
  height: 40vh;
  min-height: 240px;
}

.locate-btn {
  position: absolute;
  bottom: 16px;
  right: 16px;
  z-index: 1000;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background: rgba(26, 20, 16, 0.92);
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s;
}

.locate-btn:hover {
  background: rgba(44, 35, 28, 0.96);
}

.locate-btn .material-icons {
  font-size: 20px;
  color: #d6b36a;
  transition: transform 0.6s linear;
}

.locate-btn.locating .material-icons {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>
