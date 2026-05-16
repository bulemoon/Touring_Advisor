<template>
  <div class="app">
    <header class="top-bar">
      <div class="brand-block">
        <div class="brand-kicker">TOURING ADVISOR</div>
        <div class="logo">高端旅居顾问</div>
      </div>
      <img class="avatar-btn" src="https://via.placeholder.com/36" @click="showDrawer = true" />
    </header>

    <MapArea @located="onLocated" />

    <ChatSection :lat="lat" :lng="lng" />

    <!-- <TourSection :lat="lat" :lng="lng" @select-tour="selectedTourId = $event" /> -->

    <ShoppingSection :lat="lat" :lng="lng" :selected-tour-id="selectedTourId" />

    <AuthOverlay :visible="auth.showLogin" />

    <UserDrawer :visible="showDrawer" @close="showDrawer = false" />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { useAuthStore } from "./stores/auth"
import MapArea from "./components/MapArea.vue"
import ChatSection from "./components/ChatSection.vue"
// import TourSection from "./components/TourSection.vue"
import ShoppingSection from "./components/ShoppingSection.vue"
import AuthOverlay from "./components/AuthOverlay.vue"
import UserDrawer from "./components/UserDrawer.vue"

const auth = useAuthStore()
const showDrawer = ref(false)
const lat = ref(39.9042)
const lng = ref(116.4074)
const selectedTourId = ref<number | null>(null)

function onLocated(l: number, n: number) {
  lat.value = l
  lng.value = n
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  background:
    radial-gradient(circle at top, rgba(166, 146, 89, 0.18), transparent 32%),
    linear-gradient(180deg, #0d0b09 0%, #16110d 42%, #0a0908 100%);
}

body {
  font-family: "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif;
  background: transparent;
  -webkit-font-smoothing: antialiased;
  color: #f7f1e3;
}

.app {
  max-width: 480px;
  margin: 0 auto;
  min-height: 100vh;
  background: linear-gradient(180deg, rgba(31, 24, 19, 0.96) 0%, rgba(12, 10, 9, 1) 100%);
  box-shadow: 0 0 0 1px rgba(191, 160, 92, 0.16), 0 24px 80px rgba(0, 0, 0, 0.5);
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 18px 12px;
  background: linear-gradient(180deg, rgba(43, 33, 26, 0.96) 0%, rgba(22, 18, 15, 0.92) 100%);
  border-bottom: 1px solid rgba(201, 170, 102, 0.18);
  color: #fff7e5;
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(18px);
}

.brand-block {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.brand-kicker {
  font-size: 10px;
  letter-spacing: 0.22em;
  color: rgba(223, 196, 139, 0.72);
}

.logo {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.04em;
}

.avatar-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1px solid rgba(219, 190, 125, 0.52);
  cursor: pointer;
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.3);
}
</style>
