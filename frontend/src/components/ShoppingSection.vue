<template>
  <div class="shopping-section">
    <div class="shopping-header">
      <div>
        <div class="section-kicker">CURATED LIFESTYLE</div>
        <h3 class="section-title">会员精选周边</h3>
      </div>
      <button class="ai-btn" @click="handleAiRecommend">AI 严选</button>
    </div>

    <div class="product-list">
      <div v-for="item in products" :key="item.id" class="product-card">
        <div class="product-img">礼</div>
        <div class="product-body">
          <div class="product-name-row">
            <div class="product-name">{{ item.name }}</div>
            <div class="product-price">¥{{ item.price }}</div>
          </div>
          <div class="product-shop">{{ item.shop_name }}</div>
          <div v-if="item.reason" class="product-reason">{{ item.reason }}</div>
          <div class="product-actions">
            <button class="action-btn cart-btn" @click="handleAddCart(item)">加入购物车</button>
            <button class="action-btn order-btn" @click="handleQuickOrder(item)">立即下单</button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="cart.totalCount() > 0" class="cart-float-bar" @click="cart.showCart = true">
      <span>已选 {{ cart.totalCount() }} 件 · ¥{{ cart.totalAmount().toFixed(2) }}</span>
      <span class="checkout-label">查看购物车</span>
    </div>

    <BottomSheet :visible="cart.showCart" height="60vh" @close="cart.showCart = false">
      <div class="cart-sheet-kicker">MEMBER CART</div>
      <h3 class="cart-sheet-title">购物车</h3>
      <div v-for="item in cart.items" :key="item.id" class="cart-item">
        <span>{{ item.product_name }} × {{ item.quantity }}</span>
        <span>¥{{ (item.price * item.quantity).toFixed(2) }}</span>
        <button class="remove-btn" @click="handleRemove(item.id)">删除</button>
      </div>
      <div class="cart-total">合计：¥{{ cart.totalAmount().toFixed(2) }}</div>
      <button class="checkout-btn" @click="showOrderForm = true">提交结算</button>
    </BottomSheet>

    <BottomSheet :visible="showOrderForm" height="50vh" @close="showOrderForm = false">
      <div class="cart-sheet-kicker">ORDER DETAILS</div>
      <h3 class="cart-sheet-title">收货信息</h3>
      <div class="order-form">
        <div class="form-field">
          <label>收件人</label>
          <input v-model="orderForm.name" placeholder="请输入收件人姓名" />
        </div>
        <div class="form-field">
          <label>联系电话</label>
          <input v-model="orderForm.phone" placeholder="请输入手机号" />
        </div>
        <div class="form-field">
          <label>收货地址</label>
          <input v-model="orderForm.address" placeholder="省/市/区/详细地址" />
        </div>
        <div class="form-field">
          <label>备注</label>
          <input v-model="orderForm.note" placeholder="选填" />
        </div>
        <div class="order-summary">
          共 {{ cart.totalCount() }} 件 · 合计 ¥{{ cart.totalAmount().toFixed(2) }}
        </div>
        <button class="checkout-btn" :disabled="submitting" @click="handleSubmitOrder">
          {{ submitting ? "提交中..." : "确认下单" }}
        </button>
      </div>
    </BottomSheet>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue"
import { useCartStore } from "../stores/cart"
import { useAuthStore } from "../stores/auth"
import BottomSheet from "./BottomSheet.vue"

const props = defineProps<{ lat: number; lng: number }>()
const API = () => window.CONFIG?.API_BASE_URL || ""

const cart = useCartStore()
const auth = useAuthStore()
const products = ref<any[]>([])
const loading = ref(false)

async function fetchProducts() {
  loading.value = true
  try {
    const res = await fetch(`${API()}/api/products?lat=${props.lat}&lng=${props.lng}`)
    products.value = await res.json()
  } catch {
    products.value = []
  }
  loading.value = false
}

watch(() => [props.lat, props.lng], fetchProducts, { immediate: true })

async function handleAddCart(item: any) {
  if (!auth.token) {
    auth.showLogin = true
    return
  }
  await cart.addItem(auth.token, { product_name: item.name, price: item.price, shop_name: item.shop_name })
}

async function handleQuickOrder(item: any) {
  if (!auth.token) {
    auth.showLogin = true
    return
  }
  alert(`下单成功，订单已加入：${item.name} ¥${item.price}`)
}

async function handleRemove(id: number) {
  if (!auth.token) return
  await cart.removeItem(auth.token, id)
}

async function handleAiRecommend() {
  try {
    const res = await fetch(`${API()}/api/products/ai-recommend?lat=${props.lat}&lng=${props.lng}`)
    const data = await res.json()
    if (data.length) products.value = data
  } catch {}
}

function handleCheckout() {
  showOrderForm.value = true
}

const showOrderForm = ref(false)
const submitting = ref(false)
const orderForm = ref({ name: "", phone: "", address: "", note: "" })

async function handleSubmitOrder() {
  if (!auth.token) {
    auth.showLogin = true
    return
  }
  if (!orderForm.value.name || !orderForm.value.phone || !orderForm.value.address) {
    alert("请填写完整的收货信息")
    return
  }
  submitting.value = true
  try {
    const res = await fetch(`${API()}/api/orders`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${auth.token}` },
      body: JSON.stringify({
        items: cart.items.map(i => ({ product_name: i.product_name, price: i.price, quantity: i.quantity })),
        name: orderForm.value.name,
        phone: orderForm.value.phone,
        address: orderForm.value.address,
        note: orderForm.value.note,
      }),
    })
    if (res.ok) {
      cart.items = []
      cart.showCart = false
      showOrderForm.value = false
      orderForm.value = { name: "", phone: "", address: "", note: "" }
      alert("下单成功！")
    } else {
      alert("下单失败，请重试")
    }
  } catch {
    alert("网络异常，请稍后重试")
  }
  submitting.value = false
}

watch(() => auth.token, (t) => {
  if (t) cart.fetchCart(t)
}, { immediate: true })
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

.product-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.product-card {
  display: flex;
  gap: 12px;
  padding: 14px;
  border-radius: 24px;
  background: linear-gradient(180deg, rgba(34, 27, 22, 0.98) 0%, rgba(18, 14, 12, 1) 100%);
  border: 1px solid rgba(201, 168, 98, 0.16);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.2);
}

.product-img {
  width: 78px;
  height: 78px;
  background: linear-gradient(180deg, #4b3b2a 0%, #241c16 100%);
  border-radius: 18px;
  border: 1px solid rgba(205, 173, 105, 0.18);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  color: #d6b46c;
  flex-shrink: 0;
}

.product-body {
  flex: 1;
}

.product-name-row {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: baseline;
}

.product-name {
  font-size: 16px;
  font-weight: 600;
  color: #fff3dc;
}

.product-price {
  color: #ddb869;
  font-weight: 700;
  font-size: 22px;
  margin: 2px 0;
}

.product-shop {
  font-size: 12px;
  color: rgba(255, 240, 208, 0.55);
  margin-top: 4px;
}

.product-reason {
  font-size: 12px;
  color: #d0b06f;
  margin: 8px 0 0;
  line-height: 1.6;
}

.product-actions {
  display: flex;
  gap: 8px;
  margin-top: 10px;
}

.action-btn {
  flex: 1;
  padding: 10px 0;
  border: none;
  border-radius: 999px;
  font-size: 13px;
  cursor: pointer;
  font-weight: 700;
}

.cart-btn {
  background: rgba(255, 246, 222, 0.06);
  color: #e4c57c;
  border: 1px solid rgba(201, 168, 99, 0.14);
}

.order-btn {
  background: linear-gradient(180deg, #d8bf79 0%, #b38a3f 100%);
  color: #2a1f12;
}

.cart-float-bar {
  position: fixed;
  bottom: 12px;
  left: 50%;
  transform: translateX(-50%);
  width: min(448px, calc(100vw - 24px));
  background: linear-gradient(180deg, rgba(43, 33, 25, 0.96) 0%, rgba(20, 15, 13, 0.98) 100%);
  color: #f8edcf;
  padding: 14px 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  z-index: 500;
  border-radius: 18px;
  border: 1px solid rgba(204, 173, 106, 0.18);
  box-shadow: 0 18px 44px rgba(0, 0, 0, 0.34);
}

.checkout-label {
  color: #e0bf76;
  font-weight: 700;
}

.cart-sheet-kicker {
  font-size: 11px;
  letter-spacing: 0.16em;
  color: #ba9958;
  margin-bottom: 8px;
}

.cart-sheet-title {
  color: #f7ecd7;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  padding: 10px 0;
  border-bottom: 1px solid rgba(199, 168, 100, 0.1);
  color: #f9efd8;
}

.cart-total {
  text-align: right;
  font-size: 16px;
  font-weight: 600;
  margin: 12px 0;
  color: #dfbf78;
}

.checkout-btn {
  width: 100%;
  padding: 14px;
  border: none;
  background: linear-gradient(180deg, #d8bf79 0%, #b38a3f 100%);
  color: #2a1f12;
  border-radius: 16px;
  font-size: 16px;
  font-weight: 700;
}

.remove-btn {
  background: none;
  border: none;
  color: #d9b86d;
  font-size: 12px;
}

.order-form {
  padding: 8px 0;
}

.form-field {
  margin-bottom: 12px;
}

.form-field label {
  display: block;
  font-size: 12px;
  color: rgba(255, 240, 208, 0.6);
  margin-bottom: 4px;
}

.form-field input {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid rgba(197, 166, 100, 0.18);
  border-radius: 12px;
  font-size: 14px;
  outline: none;
  background: rgba(255, 248, 232, 0.04);
  color: #f7ead0;
}

.form-field input::placeholder {
  color: rgba(255, 241, 210, 0.35);
}

.order-summary {
  text-align: right;
  font-size: 14px;
  color: #dfbf78;
  margin: 12px 0;
  padding-top: 8px;
  border-top: 1px solid rgba(199, 168, 100, 0.1);
}

.checkout-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
