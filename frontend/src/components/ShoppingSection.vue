<template>
  <div class="shopping-section">
    <div class="shopping-header">
      <div>
        <div class="section-kicker">{{ hasItineraryShopping ? "攻略购买建议" : "周边热门推荐" }}</div>
        <h3 class="section-title">{{ hasItineraryShopping ? "旅途中可能会用到的" : "附近热门商店与去处" }}</h3>
      </div>
      <button class="ai-btn" @click="refreshList">刷新</button>
    </div>

    <div v-if="loading" class="loading-card">正在加载推荐内容...</div>
    <div v-else-if="!items.length" class="empty-card">暂时没有可展示的内容。</div>

    <div v-else class="item-list">
      <article v-for="item in items" :key="`${item.name}-${item.reason || item.address || ''}`" class="item-card">
        <div class="item-top">
          <div>
            <div class="item-title">{{ item.name }}</div>
            <div class="item-meta">{{ item.type || item.reason || "推荐内容" }}</div>
          </div>
          <div v-if="!hasItineraryShopping" class="item-distance">
            {{ formatDistance(item.distance_m ?? item.distance) }}
          </div>
        </div>

        <div v-if="item.address && item.source === 'local_shop'" class="item-address">{{ item.address }}</div>
        <div v-else-if="item.reason" class="item-reason">{{ item.reason }}</div>

        <div v-if="item.recommended_products?.length" class="chip-row">
          <span v-for="product in item.recommended_products" :key="product" class="chip">{{ product }}</span>
        </div>

        <div v-if="item.productLinks?.length" class="link-row">
          <a
            v-for="link in item.productLinks"
            :key="link.label"
            class="link-btn"
            :href="link.href"
            target="_blank"
            rel="noreferrer"
          >
            {{ link.label }}
          </a>
        </div>

        <button
          v-if="!hasItineraryShopping && hasMapTarget(item)"
          class="map-btn"
          @click="openMap(item)"
        >
          在地图中查看
        </button>
      </article>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from "vue"
import type { ShoppingRecommendation } from "../stores/chat"

type ShoppingItem = ShoppingRecommendation & {
  shop_name?: string
  image?: string
  price?: number
  product_url?: string
  reason?: string
  productLinks?: { label: string; href: string }[]
}

const props = defineProps<{
  lat: number
  lng: number
  shoppingRecommendations?: ShoppingRecommendation[]
}>()

const API = () => window.CONFIG?.API_BASE_URL || ""
const loading = ref(false)
const nearbyItems = ref<ShoppingItem[]>([])

const hasItineraryShopping = computed(() => (props.shoppingRecommendations || []).length > 0)

const items = computed<ShoppingItem[]>(() => {
  if (hasItineraryShopping.value) {
    return (props.shoppingRecommendations || []).slice(0, 8).map(item => {
      const keywords = item.purchase_keywords?.length
        ? item.purchase_keywords
        : item.recommended_products?.length
          ? item.recommended_products
          : [item.name]
      return {
        ...item,
        productLinks: item.source === "local_shop" ? [] : buildProductLinks(keywords),
      }
    })
  }
  return nearbyItems.value.slice(0, 6)
})

async function refreshList() {
  loading.value = true
  try {
    if (hasItineraryShopping.value) {
      return
    }
    const res = await fetch(`${API()}/api/products?lat=${props.lat}&lng=${props.lng}`)
    if (!res.ok) {
      nearbyItems.value = []
      return
    }
    const data = await res.json()
    nearbyItems.value = Array.isArray(data)
      ? data.map((item: any) => ({
          ...item,
          source: "nearby",
          productLinks: [],
        }))
      : []
  } catch {
    nearbyItems.value = []
  } finally {
    loading.value = false
  }
}

watch(
  () => [props.lat, props.lng, hasItineraryShopping.value, props.shoppingRecommendations],
  refreshList,
  { immediate: true, deep: true },
)

function buildProductLinks(keywords: string[]) {
  const keyword = keywords[0] || "旅行用品"
  return [
    { label: "淘宝", href: `https://s.taobao.com/search?q=${encodeURIComponent(keyword)}` },
    { label: "天猫", href: `https://list.tmall.com/search_product.htm?q=${encodeURIComponent(keyword)}` },
    { label: "京东", href: `https://search.jd.com/Search?keyword=${encodeURIComponent(keyword)}&enc=utf-8` },
  ]
}

function formatDistance(distance: string | number | undefined) {
  if (distance === undefined || distance === null || distance === "") return "附近"
  const value = typeof distance === "string" ? Number(distance) : distance
  if (!Number.isFinite(value)) return "附近"
  if (value >= 1000) return `${(value / 1000).toFixed(1)} 公里`
  return `${Math.round(value)} 米`
}

function hasMapTarget(item: ShoppingItem) {
  return Number.isFinite(item.lat) && Number.isFinite(item.lng)
}

function openMap(item: ShoppingItem) {
  const query = encodeURIComponent(item.name)
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

.loading-card,
.empty-card {
  padding: 14px 16px;
  border-radius: 16px;
  background: rgba(255, 247, 228, 0.05);
  border: 1px solid rgba(201, 168, 98, 0.16);
  color: rgba(255, 240, 208, 0.72);
  margin-bottom: 12px;
}

.item-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.item-card {
  padding: 16px;
  border-radius: 20px;
  background: linear-gradient(180deg, rgba(34, 27, 22, 0.98) 0%, rgba(18, 14, 12, 1) 100%);
  border: 1px solid rgba(201, 168, 98, 0.16);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.2);
}

.item-top {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: baseline;
}

.item-title {
  font-size: 18px;
  font-weight: 700;
  color: #fff5df;
}

.item-meta,
.item-address,
.item-reason {
  margin-top: 8px;
  font-size: 13px;
  line-height: 1.6;
  color: rgba(255, 244, 222, 0.74);
}

.item-distance {
  font-size: 13px;
  color: #d8b86d;
  white-space: nowrap;
}

.chip-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 12px;
}

.chip {
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(216, 191, 121, 0.12);
  color: #f0d9a0;
  font-size: 12px;
}

.link-row {
  display: flex;
  gap: 8px;
  margin-top: 12px;
  flex-wrap: wrap;
}

.link-btn {
  padding: 8px 12px;
  border-radius: 999px;
  text-decoration: none;
  background: rgba(255, 247, 228, 0.06);
  border: 1px solid rgba(205, 173, 106, 0.14);
  color: #f7ecd7;
  font-size: 12px;
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
