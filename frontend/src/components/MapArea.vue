<template>
  <div ref="mapContainer" class="map-area" />
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue"
import L from "leaflet"
import "leaflet/dist/leaflet.css"

const emit = defineEmits<{ located: [lat: number, lng: number] }>()

const mapContainer = ref<HTMLDivElement>()
let map: L.Map | null = null

onMounted(() => {
  if (!mapContainer.value) return
  map = L.map(mapContainer.value, {
    zoomControl: false,
    attributionControl: false,
  }).setView([39.9042, 116.4074], 13)

  L.tileLayer("https://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}", {
    maxZoom: 18,
  }).addTo(map)

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        const { latitude, longitude } = pos.coords
        map?.setView([latitude, longitude], 14)
        L.marker([latitude, longitude]).addTo(map!)
          .bindPopup("我的位置")
          .openPopup()
        emit("located", latitude, longitude)
      },
      () => {
        L.marker([39.9042, 116.4074]).addTo(map!)
          .bindPopup("默认位置：北京")
        emit("located", 39.9042, 116.4074)
      }
    )
  } else {
    emit("located", 39.9042, 116.4074)
  }
})

onUnmounted(() => {
  map?.remove()
})
</script>

<style scoped>
.map-area {
  width: 100%;
  height: 40vh;
  min-height: 240px;
}
</style>
