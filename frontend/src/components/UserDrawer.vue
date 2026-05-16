<template>
  <Teleport to="body">
    <div v-if="visible" class="drawer-overlay" @click.self="$emit('close')">
      <div class="drawer">
        <div class="drawer-header">
          <img :src="avatarUrl || 'https://via.placeholder.com/60'" class="avatar" />
          <div>
            <div class="nickname">{{ nickname || "旅行者" }}</div>
            <div class="phone">{{ phone }}</div>
          </div>
        </div>
        <div v-if="!currentView" class="drawer-menu">
          <div class="menu-item" @click="currentView = 'history'">📋 我的行程</div>
          <div class="menu-item" @click="currentView = 'orders'">📦 我的订单</div>
          <div class="menu-item" @click="currentView = 'favorites'">❤️ 收藏夹</div>
          <div class="menu-item menu-logout" @click="handleLogout">🚪 退出登录</div>
        </div>
        <div v-else class="drawer-subview">
          <button class="back-btn" @click="currentView = ''">← 返回</button>
          <div class="subview-content scrollable">
            <template v-if="currentView === 'history'">
              <div v-if="loading" class="loading-text">加载中...</div>
              <div v-else-if="!itineraries.length" class="empty-text">暂无行程记录</div>
              <div v-for="(item, i) in itineraries" :key="i" class="list-card">
                <div class="list-card-name">{{ item.title }}</div>
                <div class="list-card-meta">{{ item.date }} · {{ item.stops }} 站</div>
              </div>
            </template>
            <template v-if="currentView === 'orders'">
              <div v-if="loading" class="loading-text">加载中...</div>
              <div v-else-if="!orders.length" class="empty-text">暂无订单</div>
              <div v-for="(item, i) in orders" :key="i" class="list-card" @click="selectedOrder = selectedOrder?.id === item.id ? null : item">
                <div class="list-card-name">{{ item.product_name || `订单 #${item.id}` }}</div>
                <div class="list-card-meta">{{ item.created_at }} · ¥{{ item.total }}</div>
                <div :class="['order-status', item.status]">{{ statusLabel(item.status) }}</div>
                <div v-if="selectedOrder?.id === item.id" class="order-detail">
                  <div v-if="item.name">收件人：{{ item.name }}</div>
                  <div v-if="item.address">地址：{{ item.address }}</div>
                  <div v-if="item.phone">电话：{{ item.phone }}</div>
                  <div v-if="item.note">备注：{{ item.note }}</div>
                </div>
              </div>
            </template>
            <template v-if="currentView === 'favorites'">
              <div v-if="loading" class="loading-text">加载中...</div>
              <div v-else-if="!favorites.length" class="empty-text">收藏夹为空</div>
              <div v-for="(item, i) in favorites" :key="i" class="list-card">
                <div class="list-card-name">{{ item.name }}</div>
                <div class="list-card-meta">{{ item.type === 'tour' ? '路线' : '商品' }}</div>
              </div>
            </template>
          </div>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, watch } from "vue"
import { useAuthStore } from "../stores/auth"

const props = defineProps<{ visible: boolean }>()
const emit = defineEmits<{ close: [] }>()

const API = () => window.CONFIG?.API_BASE_URL || ""

const auth = useAuthStore()
const currentView = ref("")
const avatarUrl = ref("")
const nickname = ref("")
const phone = ref(String(auth.userId))

const itineraries = ref<any[]>([])
const orders = ref<any[]>([])
const favorites = ref<any[]>([])
const selectedOrder = ref<any>(null)
const loading = ref(false)

function statusLabel(s: string) {
  const map: Record<string, string> = { pending: "待处理", paid: "已付款", shipped: "已发货", done: "已完成", cancelled: "已取消" }
  return map[s] || s
}

async function fetchHistory() {
  loading.value = true
  try {
    const res = await fetch(`${API()}/api/tours?user_id=${auth.userId}`)
    if (res.ok) {
      const data = await res.json()
      itineraries.value = (data || []).map((t: any, i: number) => ({
        id: t.id || i,
        title: t.title || `行程 #${i + 1}`,
        date: t.created_at ? t.created_at.slice(0, 10) : "近期",
        stops: t.stops?.length || 0,
      }))
    }
  } catch {}
  loading.value = false
}

async function fetchOrders() {
  loading.value = true
  try {
    const res = await fetch(`${API()}/api/orders`, {
      headers: { Authorization: `Bearer ${auth.token}` },
    })
    if (res.ok) {
      orders.value = await res.json()
    }
  } catch {}
  loading.value = false
}

async function fetchFavorites() {
  loading.value = true
  try {
    const res = await fetch(`${API()}/api/tours/favorites?user_id=${auth.userId}`)
    if (res.ok) {
      favorites.value = await res.json()
    }
  } catch {}
  loading.value = false
}

watch(currentView, (v) => {
  selectedOrder.value = null
  if (v === "history") fetchHistory()
  else if (v === "orders") fetchOrders()
  else if (v === "favorites") fetchFavorites()
})

function handleLogout() {
  auth.logout()
  emit("close")
}
</script>

<style scoped>
.drawer-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1500;
}
.drawer {
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 300px;
  background: linear-gradient(180deg, #1f1914 0%, #120f0c 100%);
  animation: slideIn 0.3s ease;
  display: flex;
  flex-direction: column;
  border-left: 1px solid rgba(201, 170, 102, 0.18);
}
.drawer-header {
  padding: 24px 16px;
  background: linear-gradient(180deg, rgba(43, 33, 26, 0.96) 0%, rgba(22, 18, 15, 0.92) 100%);
  border-bottom: 1px solid rgba(201, 170, 102, 0.18);
  color: #fff7e5;
  display: flex;
  align-items: center;
  gap: 12px;
}
.avatar { width: 48px; height: 48px; border-radius: 50%; border: 2px solid rgba(219, 190, 125, 0.52); }
.nickname { font-size: 16px; font-weight: 600; color: #fff7e5; }
.phone { font-size: 13px; opacity: 0.7; color: rgba(255, 240, 208, 0.7); }
.drawer-menu { flex: 1; padding: 8px 0; }
.menu-item {
  padding: 14px 16px;
  font-size: 15px;
  cursor: pointer;
  border-bottom: 1px solid rgba(199, 168, 100, 0.08);
  color: #f0e6d0;
  transition: background 0.2s;
}
.menu-item:hover { background: rgba(255, 247, 228, 0.04); }
.menu-logout { color: #e57373; }
.drawer-subview {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 12px 0;
  overflow: hidden;
}
.back-btn {
  background: none;
  border: none;
  color: #d6b36a;
  font-size: 14px;
  padding: 8px 16px;
  cursor: pointer;
  text-align: left;
  border-bottom: 1px solid rgba(199, 168, 100, 0.08);
}
.subview-content { flex: 1; overflow-y: auto; padding: 8px 16px; }
.subview-content.scrollable { overflow-y: auto; }
.loading-text, .empty-text { color: rgba(255, 240, 208, 0.5); text-align: center; padding: 40px 0; font-size: 14px; }
.list-card {
  padding: 12px;
  margin-bottom: 8px;
  border-radius: 16px;
  background: rgba(34, 27, 22, 0.98);
  border: 1px solid rgba(201, 168, 98, 0.12);
  cursor: pointer;
}
.list-card-name { font-size: 14px; font-weight: 600; color: #fff3dc; }
.list-card-meta { font-size: 12px; color: rgba(255, 240, 208, 0.5); margin-top: 4px; }
.order-status { font-size: 12px; margin-top: 4px; }
.order-status.pending { color: #ffb74d; }
.order-status.paid { color: #81c784; }
.order-status.shipped { color: #64b5f6; }
.order-status.done { color: #a5d6a7; }
.order-status.cancelled { color: #e57373; }
.order-detail {
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px solid rgba(199, 168, 100, 0.1);
  font-size: 12px;
  color: rgba(255, 240, 208, 0.7);
  line-height: 1.7;
}
@keyframes slideIn {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}
</style>
