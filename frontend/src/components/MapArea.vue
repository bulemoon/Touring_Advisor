<template>
  <div class="map-wrapper">
    <div ref="mapContainer" class="map-area" />
    <button class="locate-btn" @click="relocate" :class="{ locating }" title="定位到当前位置">
      <span class="material-icons">my_location</span>
    </button>
  </div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref, watch } from "vue"
import L from "leaflet"
import "leaflet/dist/leaflet.css"
import type { RouteDay, RoutePlan, RouteStop } from "../stores/chat"

const props = defineProps<{ routePlan: RoutePlan | null }>()
const emit = defineEmits<{ located: [lat: number, lng: number] }>()

const mapContainer = ref<HTMLDivElement>()
const locating = ref(false)

let map: L.Map | null = null
let currentMarker: L.Marker | null = null
let routeLayer: L.LayerGroup | null = null
let forceFocusLocation = false

const DEFAULT_LAT = 39.9042
const DEFAULT_LNG = 116.4074
const DAY_COLORS = ["#2f80ed", "#eb5757", "#27ae60", "#f2994a", "#9b51e0", "#00a6a6"]

const locationIcon = L.icon({
  iconUrl: "/icons/location-pin.svg",
  iconSize: [36, 36],
  iconAnchor: [18, 36],
  popupAnchor: [0, -36],
})

function hasRoutePlan(routePlan: RoutePlan | null) {
  return normalizeRouteDays(routePlan).length > 0
}

function addLocationMarker(lat: number, lng: number, label: string) {
  if (!map) return null
  if (currentMarker) map.removeLayer(currentMarker)
  currentMarker = L.marker([lat, lng], { icon: locationIcon })
    .addTo(map)
    .bindPopup(label)
  return currentMarker
}

function relocate() {
  if (locating.value || !map) return
  locating.value = true
  forceFocusLocation = true
  addLocationMarker(DEFAULT_LAT, DEFAULT_LNG, "定位中...")
  locateWithAmap()
}

function focusLocation(lat: number, lng: number, zoom = 14) {
  if (!map) return
  if (forceFocusLocation || !hasRoutePlan(props.routePlan)) {
    map.setView([lat, lng], zoom)
    currentMarker?.openPopup()
  }
  forceFocusLocation = false
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
    if (data.success) {
      addLocationMarker(data.lat, data.lng, `${data.city || "当前城市"}（IP 定位）`)
      focusLocation(data.lat, data.lng, 11)
      emit("located", data.lat, data.lng)
      return
    }
  } catch (e) {
    console.warn("[IP Geo] failed:", e)
  }
  addLocationMarker(DEFAULT_LAT, DEFAULT_LNG, "无法定位，使用默认位置")
  focusLocation(DEFAULT_LAT, DEFAULT_LNG, 11)
  emit("located", DEFAULT_LAT, DEFAULT_LNG)
}

function fallbackToNativeGeo() {
  if (!navigator.geolocation) {
    fallbackToIpLocation()
    return
  }
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      locating.value = false
      const [lat, lng] = wgs84ToGcj02(pos.coords.latitude, pos.coords.longitude)
      addLocationMarker(lat, lng, `我的位置<br/>${lat.toFixed(5)}, ${lng.toFixed(5)}`)
      focusLocation(lat, lng)
      emit("located", lat, lng)
    },
    (err) => {
      console.warn("[Geo] native location failed:", err.code, err.message)
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
      addLocationMarker(lat, lng, `我的位置<br/>${lat.toFixed(5)}, ${lng.toFixed(5)}`)
      focusLocation(lat, lng)
      emit("located", lat, lng)
    } else {
      console.warn("[AMap] location failed:", result?.info, result?.message)
      fallbackToNativeGeo()
    }
  })
}

function redrawRoutePlan(routePlan: RoutePlan | null) {
  if (!map || !routeLayer) return
  routeLayer.clearLayers()

  const days = normalizeRouteDays(routePlan)
  if (!days.length) return

  const boundsPoints: L.LatLngExpression[] = []

  days.forEach((day, dayIndex) => {
    const color = DAY_COLORS[dayIndex % DAY_COLORS.length]
    const stops = day.stops.filter(isValidStop)

    stops.forEach((stop, stopIndex) => {
      boundsPoints.push([stop.lat, stop.lng])
      const marker = L.marker([stop.lat, stop.lng], {
        icon: createRouteIcon(day.day, stopIndex + 1, color),
      }).bindPopup(createStopPopup(day.day, stopIndex + 1, stop))
      routeLayer?.addLayer(marker)
    })

    const linePoints = getDayPolyline(day, stops)
    if (linePoints.length >= 2) {
      linePoints.forEach(point => boundsPoints.push(point))
      routeLayer?.addLayer(L.polyline(linePoints, {
        color,
        weight: 4,
        opacity: 0.92,
        lineJoin: "round",
      }))
    }
  })

  if (boundsPoints.length > 0) {
    map.fitBounds(L.latLngBounds(boundsPoints), { padding: [30, 30], maxZoom: 15 })
  }
}

function normalizeRouteDays(routePlan: RoutePlan | null): RouteDay[] {
  if (!routePlan) return []
  const days = (routePlan.days || [])
    .map(day => ({ ...day, stops: day.stops || [] }))
    .filter(day => day.stops.some(isValidStop))
  if (days.length > 0) return days

  const stops = (routePlan.stops || []).filter(isValidStop)
  return stops.length > 0 ? [{ day: 1, stops }] : []
}

function getDayPolyline(day: RouteDay, stops: RouteStop[]): L.LatLngExpression[] {
  if (day.polyline?.length) {
    return day.polyline.filter(isValidPoint).map(point => [point[0], point[1]])
  }

  const segmentPoints = (day.segments || [])
    .flatMap(segment => segment.polyline || [])
    .filter(isValidPoint)
    .map(point => [point[0], point[1]] as L.LatLngExpression)
  if (segmentPoints.length) return segmentPoints

  return stops.map(stop => [stop.lat, stop.lng] as L.LatLngExpression)
}

function createRouteIcon(day: number, order: number, color: string) {
  return L.divIcon({
    className: "route-marker",
    html: `<div style="--route-color:${color}"><span>D${day}</span><strong>${order}</strong></div>`,
    iconSize: [34, 42],
    iconAnchor: [17, 42],
    popupAnchor: [0, -38],
  })
}

function createStopPopup(day: number, order: number, stop: RouteStop) {
  const duration = formatDuration(stop.duration_minutes)
  const address = stop.address || "暂无地址"
  const tip = stop.tip || "来自本次行程推荐"
  return `
    <div class="route-popup">
      <strong>第${formatChineseNumber(day)}天 - 第${formatChineseNumber(order)}站</strong>
      <div>${escapeHtml(stop.name)}</div>
      <small>${escapeHtml(address)}</small>
      <small>停留：${escapeHtml(duration)}</small>
      <small>${escapeHtml(tip)}</small>
    </div>
  `
}

function formatDuration(minutes?: number) {
  if (!Number.isFinite(minutes) || !minutes || minutes <= 0) return "按行程安排"
  const wholeMinutes = Math.round(minutes)
  const hours = Math.floor(wholeMinutes / 60)
  const restMinutes = wholeMinutes % 60
  if (hours > 0 && restMinutes > 0) return `${hours}小时${restMinutes}分钟`
  if (hours > 0) return `${hours}小时`
  return `${restMinutes}分钟`
}

function formatChineseNumber(value: number) {
  const digits = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
  if (value >= 0 && value <= 9) return digits[value]
  if (value === 10) return "十"
  if (value > 10 && value < 20) return `十${digits[value % 10]}`
  if (value < 100) {
    const ten = Math.floor(value / 10)
    const one = value % 10
    return `${digits[ten]}十${one ? digits[one] : ""}`
  }
  return String(value)
}

function isValidStop(stop: RouteStop) {
  return Number.isFinite(stop.lat) && Number.isFinite(stop.lng)
}

function isValidPoint(point: [number, number]) {
  return Array.isArray(point) && Number.isFinite(point[0]) && Number.isFinite(point[1])
}

function escapeHtml(value: string) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;")
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

  routeLayer = L.layerGroup().addTo(map)
  addLocationMarker(DEFAULT_LAT, DEFAULT_LNG, "默认位置")
  redrawRoutePlan(props.routePlan)

  if (!hasRoutePlan(props.routePlan)) {
    try {
      await loadAmapScript()
      locateWithAmap()
    } catch {
      fallbackToIpLocation()
    }
  }
})

watch(() => props.routePlan, redrawRoutePlan, { deep: true })

onUnmounted(() => {
  map?.remove()
  map = null
  routeLayer = null
  currentMarker = null
})

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

:deep(.route-marker) {
  background: transparent;
  border: none;
}

:deep(.route-marker div) {
  width: 34px;
  height: 42px;
  color: #fff;
  background: var(--route-color);
  border: 2px solid rgba(255, 255, 255, 0.9);
  border-radius: 17px 17px 17px 4px;
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.28);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transform: rotate(-45deg);
}

:deep(.route-marker span),
:deep(.route-marker strong) {
  display: block;
  line-height: 1;
  transform: rotate(45deg);
}

:deep(.route-marker span) {
  font-size: 9px;
  font-weight: 700;
  opacity: 0.85;
}

:deep(.route-marker strong) {
  margin-top: 2px;
  font-size: 15px;
}

:deep(.route-popup) {
  min-width: 160px;
  color: #2b241b;
}

:deep(.route-popup strong),
:deep(.route-popup div),
:deep(.route-popup small) {
  display: block;
}

:deep(.route-popup strong) {
  margin-bottom: 6px;
  color: #9a6a18;
}

:deep(.route-popup div) {
  margin-bottom: 4px;
  font-weight: 700;
}

:deep(.route-popup small) {
  margin-top: 3px;
  color: #5f564c;
  line-height: 1.45;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>
