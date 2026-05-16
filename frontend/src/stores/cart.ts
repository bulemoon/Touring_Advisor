import { defineStore } from "pinia"
import { ref } from "vue"

const API = () => window.CONFIG?.API_BASE_URL || ""

interface CartItem {
  id: number
  product_name: string
  product_image: string
  price: number
  quantity: number
  shop_name: string
}

export const useCartStore = defineStore("cart", () => {
  const items = ref<CartItem[]>([])
  const showCart = ref(false)

  const totalCount = () => items.value.reduce((s, i) => s + i.quantity, 0)
  const totalAmount = () => items.value.reduce((s, i) => s + i.price * i.quantity, 0)

  async function fetchCart(token: string) {
    const res = await fetch(`${API()}/api/cart`, {
      headers: { Authorization: `Bearer ${token}` },
    })
    items.value = await res.json()
  }

  async function addItem(token: string, product: { product_name: string; price: number; shop_name?: string }) {
    const res = await fetch(`${API()}/api/cart`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
      body: JSON.stringify(product),
    })
    const item = await res.json()
    items.value.push(item)
  }

  async function removeItem(token: string, id: number) {
    await fetch(`${API()}/api/cart/${id}`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${token}` },
    })
    items.value = items.value.filter((i) => i.id !== id)
  }

  return { items, showCart, totalCount, totalAmount, fetchCart, addItem, removeItem }
})
