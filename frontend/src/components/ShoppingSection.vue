<template>
  <div class="shopping-section">
    <div class="shopping-header">
      <div>
        <div class="section-kicker">ROUTE HIGHLIGHTS</div>
        <h3 class="section-title">路线关键地点</h3>
      </div>
      <button class="ai-btn" @click="refreshHighlights">更新建议</button>
    </div>

    <div v-if="loading" class="loading-card">正在根据路线和附近地点生成建议...</div>

    <div class="highlight-list">
      <article v-for="item in highlights" :key="item.title" class="highlight-card" @click="openMap(item)">
        <div class="highlight-cover" :style="coverStyle(item.cover_url)">
          <div class="highlight-cover-badge">地点推荐</div>
        </div>
        <div class="highlight-body">
          <div class="highlight-title-row">
            <div class="highlight-title">{{ item.title }}</div>
            <div class="highlight-distance">{{ formatDistance(item.distance_m) }}</div>
          </div>
          <div class="highlight-address">{{ item.address }}</div>
          <div class="highlight-intro">{{ item.intro }}</div>
          <div class="highlight-keyword">知乎关键词：{{ item.zhihu_keyword }}</div>
          <div v-if="item.zhihu_notes?.length" class="zhihu-list">
            <a
              v-for="note in item.zhihu_notes.slice(0, 2)"
              :key="note.url || note.title"
              class="zhihu-item"
              :href="note.url || '#'"
              target="_blank"
              rel="noreferrer"
              @click.stop
            >
              <div class="zhihu-item-title">{{ note.title }}</div>
              <div class="zhihu-item-summary">{{ note.summary }}</div>
            </a>
          </div>
          <button class="map-btn" @click.stop="openMap(item)">在地图中查看</button>
        </div>
      </article>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue"

const props = defineProps<{ lat: number; lng: number; selectedTourId?: number | null }>()
const API = () => window.CONFIG?.API_BASE_URL || ""

const loading = ref(false)
const highlights = ref<any[]>([])

const mockHighlights = [
  {
    title: "滴水湖",
    address: "上海市浦东新区南汇新城镇环湖西一路",
    distance_m: 1200,
    cover_url:
      "https://restapi.amap.com/v3/staticmap?location=121.9298,30.9023&zoom=15&size=640*360&scale=2&markers=mid,0xD8BF79,A:121.9298,30.9023",
    intro: "适合作为临港路线的开场点，湖景开阔，日落和骑行体验都稳定。",
    zhihu_keyword: "上海临港 滴水湖",
    zhihu_notes: [
      {
        title: "滴水湖值得怎么逛",
        summary: "看日落、骑行、湖边散步是最稳的玩法。",
        url: "",
      },
    ],
    lat: 30.9023,
    lng: 121.9298,
  },
  {
    title: "中国航海博物馆",
    address: "上海市浦东新区申港大道197号",
    distance_m: 2600,
    cover_url:
      "https://restapi.amap.com/v3/staticmap?location=121.9186,30.9075&zoom=15&size=640*360&scale=2&markers=mid,0xD8BF79,A:121.9186,30.9075",
    intro: "适合接在滴水湖之后，内容完整，室内参观也更稳，适合半日路线收束。",
    zhihu_keyword: "上海临港 航海博物馆",
    zhihu_notes: [
      {
        title: "航海博物馆参观体验",
        summary: "适合拍建筑外观，也适合带着主题逛展。",
        url: "",
      },
    ],
    lat: 30.9075,
    lng: 121.9186,
  },
]

async function refreshHighlights() {
  const tourId = props.selectedTourId
  if (!tourId) {
    highlights.value = mockHighlights
    return
  }

  loading.value = true
  try {
    const res = await fetch(`${API()}/api/tours/${tourId}/highlights?lat=${props.lat}&lng=${props.lng}`)
    if (!res.ok) {
      highlights.value = mockHighlights
      return
    }
    const data = await res.json()
    highlights.value = data.highlights?.length ? data.highlights : mockHighlights
  } catch {
    highlights.value = mockHighlights
  } finally {
    loading.value = false
  }
}

watch(() => [props.lat, props.lng, props.selectedTourId], refreshHighlights, { immediate: true })

function coverStyle(url: string) {
  return url
    ? { backgroundImage: `linear-gradient(180deg, rgba(24,18,14,.08), rgba(24,18,14,.56)), url(${url})` }
    : {}
}

function formatDistance(distance: number) {
  if (!distance) return "附近"
  if (distance >= 1000) return `${(distance / 1000).toFixed(1)} km`
  return `${distance} m`
}

function openMap(item: any) {
  const query = encodeURIComponent(item.title)
  window.open(`https://uri.amap.com/marker?position=${item.lng},${item.lat}&name=${query}`, "_blank")
}
</script>

<style scoped>
.shopping-section {
  padding: 16px;
  background: transparent;
  padding-bottom: 92px;
}

.shopping-header {
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

.ai-btn {
  padding: 9px 16px;
  border: 1px solid rgba(204, 173, 106, 0.2);
  background: rgba(255, 247, 228, 0.05);
  color: #e0c27a;
  border-radius: 999px;
  font-size: 13px;
}

.loading-card {
  padding: 14px 16px;
  border-radius: 18px;
  background: rgba(255, 247, 228, 0.05);
  border: 1px solid rgba(201, 168, 98, 0.16);
  color: rgba(255, 240, 208, 0.72);
  margin-bottom: 12px;
}

.highlight-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.highlight-card {
  overflow: hidden;
  border-radius: 24px;
  background: linear-gradient(180deg, rgba(34, 27, 22, 0.98) 0%, rgba(18, 14, 12, 1) 100%);
  border: 1px solid rgba(201, 168, 98, 0.16);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.2);
}

.highlight-cover {
  height: 168px;
  background-color: #3b3129;
  background-size: cover;
  background-position: center;
  position: relative;
}

.highlight-cover::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(255, 244, 219, 0.03), rgba(0, 0, 0, 0.36));
}

.highlight-cover-badge {
  position: absolute;
  top: 14px;
  left: 14px;
  z-index: 1;
  padding: 7px 12px;
  border-radius: 999px;
  background: rgba(24, 18, 14, 0.72);
  color: #f0d9a0;
  border: 1px solid rgba(210, 180, 111, 0.18);
  font-size: 12px;
}

.highlight-body {
  padding: 16px;
}

.highlight-title-row {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: baseline;
}

.highlight-title {
  font-size: 20px;
  font-weight: 700;
  color: #fff5df;
}

.highlight-distance {
  font-size: 13px;
  color: #d8b86d;
  white-space: nowrap;
}

.highlight-address,
.highlight-intro,
.highlight-keyword {
  margin-top: 8px;
  font-size: 13px;
  line-height: 1.6;
  color: rgba(255, 244, 222, 0.74);
}

.highlight-keyword {
  color: #d0b06f;
}

.zhihu-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 12px;
}

.zhihu-item {
  display: block;
  padding: 12px;
  border-radius: 16px;
  text-decoration: none;
  background: rgba(255, 247, 228, 0.04);
  border: 1px solid rgba(205, 173, 106, 0.12);
}

.zhihu-item-title {
  font-size: 13px;
  font-weight: 700;
  color: #f7ecd7;
}

.zhihu-item-summary {
  margin-top: 4px;
  font-size: 12px;
  line-height: 1.6;
  color: rgba(255, 240, 208, 0.62);
}

.map-btn {
  margin-top: 12px;
  width: 100%;
  padding: 12px 0;
  border: none;
  border-radius: 999px;
  background: linear-gradient(180deg, #d8bf79 0%, #b38a3f 100%);
  color: #2a1f12;
  font-size: 14px;
  font-weight: 700;
}
</style>
