<template>
  <div class="tour-section">
    <div class="section-head">
      <div>
        <div class="section-kicker">PRIVATE ITINERARY</div>
        <h3 class="section-title">甄选路线</h3>
      </div>
      <div class="section-badge">会员优先</div>
    </div>

    <div class="tour-tabs">
      <button
        v-for="tab in tabs"
        :key="tab.key"
        :class="['tab-btn', { active: activeTab === tab.key }]"
        @click="activeTab = tab.key"
      >
        {{ tab.label }}
      </button>
    </div>

    <div class="tour-cards">
      <div
        v-for="tour in filteredTours"
        :key="tour.id"
        class="tour-card"
        @click="selectedTour = tour"
      >
        <div class="tour-card-media" :style="{ background: bgColors[tour.id % bgColors.length] }">
          <div class="tour-card-chip">礼宾推荐</div>
        </div>
        <div class="tour-card-body">
          <div class="tour-card-title-row">
            <div class="tour-card-title">{{ tour.title }}</div>
            <div class="tour-card-score">4.9</div>
          </div>
          <div class="tour-card-summary">
            {{ tour.description || "覆盖人文、景观点位与舒适步行节奏。" }}
          </div>
          <div class="tour-card-meta-row">
            <div class="tour-card-meta">收藏 {{ tour.favorites_count }}</div>
            <div class="tour-card-meta">{{ durationLabel(tour.duration) }}</div>
          </div>
        </div>
      </div>
    </div>

    <BottomSheet :visible="!!selectedTour" height="60vh" @close="selectedTour = null">
      <div class="detail-kicker">ROUTE DETAIL</div>
      <h3 class="detail-title">{{ selectedTour?.title }}</h3>
      <p class="detail-copy">{{ selectedTour?.description }}</p>
      <button class="fav-btn" @click="handleFavorite">加入会员收藏</button>
    </BottomSheet>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from "vue"
import BottomSheet from "./BottomSheet.vue"

const props = defineProps<{ lat: number; lng: number }>()
const API = () => window.CONFIG?.API_BASE_URL || ""

const tabs = [
  { key: "half-day", label: "半日精选" },
  { key: "1-day", label: "一日漫游" },
  { key: "3-day", label: "三日深度" },
]

const activeTab = ref("half-day")
const selectedTour = ref<any>(null)
const allTours = ref<any[]>([])
const loading = ref(false)

const bgColors = ["#6f5631", "#4b4337", "#61472d", "#3e352d", "#765b33"]

const filteredTours = computed(() => allTours.value.filter((t) => t.duration === activeTab.value))

async function fetchTours() {
  loading.value = true
  try {
    const res = await fetch(`${API()}/api/tours?lat=${props.lat}&lng=${props.lng}`)
    allTours.value = await res.json()
  } catch {
    allTours.value = []
  }
  loading.value = false
}

watch(() => [props.lat, props.lng], fetchTours, { immediate: true })

function handleFavorite() {
  if (selectedTour.value) {
    selectedTour.value.favorites_count++
  }
}

function durationLabel(duration: string) {
  if (duration === "half-day") return "建议 2-4 小时"
  if (duration === "1-day") return "建议 1 天"
  if (duration === "3-day") return "建议 3 天"
  return "灵活安排行程"
}
</script>

<style scoped>
.tour-section {
  padding: 16px;
  background: transparent;
}

.section-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 14px;
}

.section-kicker {
  font-size: 11px;
  letter-spacing: 0.18em;
  color: #b99856;
  margin-bottom: 6px;
}

.section-title {
  margin: 0;
  font-size: 24px;
  color: #fff4df;
}

.section-badge {
  padding: 6px 12px;
  border-radius: 999px;
  border: 1px solid rgba(207, 175, 109, 0.22);
  background: rgba(255, 242, 210, 0.05);
  color: #dabb79;
  font-size: 12px;
}

.tour-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 14px;
  overflow-x: auto;
}

.tab-btn {
  padding: 9px 16px;
  border: 1px solid rgba(205, 174, 107, 0.18);
  border-radius: 999px;
  background: rgba(255, 249, 234, 0.04);
  font-size: 13px;
  cursor: pointer;
  color: rgba(250, 238, 213, 0.72);
  white-space: nowrap;
}

.tab-btn.active {
  background: linear-gradient(180deg, #d7bd78 0%, #b58b40 100%);
  color: #2a1f12;
  border-color: transparent;
  font-weight: 700;
}

.tour-cards {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.tour-card {
  border-radius: 24px;
  overflow: hidden;
  background: linear-gradient(180deg, rgba(34, 27, 22, 0.98) 0%, rgba(18, 14, 12, 1) 100%);
  border: 1px solid rgba(201, 168, 98, 0.18);
  cursor: pointer;
  box-shadow: 0 18px 40px rgba(0, 0, 0, 0.22);
}

.tour-card-media {
  height: 132px;
  position: relative;
  background-size: cover;
  background-position: center;
}

.tour-card-media::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(255, 240, 202, 0.05) 0%, rgba(16, 12, 10, 0.6) 100%);
}

.tour-card-chip {
  position: absolute;
  top: 14px;
  left: 14px;
  z-index: 1;
  padding: 7px 12px;
  border-radius: 999px;
  background: rgba(25, 20, 16, 0.72);
  border: 1px solid rgba(210, 180, 111, 0.18);
  color: #f0d9a0;
  font-size: 12px;
}

.tour-card-body {
  padding: 16px;
}

.tour-card-title-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
}

.tour-card-title {
  font-size: 19px;
  font-weight: 700;
  color: #fff5df;
}

.tour-card-score {
  font-size: 16px;
  font-weight: 700;
  color: #d8b86d;
}

.tour-card-summary {
  margin: 10px 0 14px;
  font-size: 14px;
  line-height: 1.7;
  color: rgba(255, 244, 222, 0.74);
}

.tour-card-meta-row {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.tour-card-meta {
  font-size: 12px;
  color: #d3b26f;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 247, 228, 0.05);
  border: 1px solid rgba(205, 173, 106, 0.14);
}

.detail-kicker {
  font-size: 11px;
  letter-spacing: 0.16em;
  color: #ba9958;
  margin-bottom: 8px;
}

.detail-title {
  color: #f7ecd7;
  margin-bottom: 10px;
}

.detail-copy {
  color: rgba(248, 235, 208, 0.78);
  line-height: 1.7;
}

.fav-btn {
  padding: 12px 24px;
  border: none;
  background: linear-gradient(180deg, #d8bf79 0%, #b38a3f 100%);
  color: #2a1f12;
  border-radius: 999px;
  font-size: 14px;
  margin-top: 12px;
  font-weight: 700;
}
</style>
