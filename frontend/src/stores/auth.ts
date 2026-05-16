import { defineStore } from "pinia"
import { ref } from "vue"

const API = () => window.CONFIG?.API_BASE_URL || ""

export const useAuthStore = defineStore("auth", () => {
  const token = ref(localStorage.getItem("token") || "")
  const userId = ref(Number(localStorage.getItem("userId") || 0))
  const showLogin = ref(!token.value)

  function setAuth(t: string, uid: number) {
    token.value = t
    userId.value = uid
    localStorage.setItem("token", t)
    localStorage.setItem("userId", String(uid))
    showLogin.value = false
  }

  function logout() {
    token.value = ""
    userId.value = 0
    localStorage.removeItem("token")
    localStorage.removeItem("userId")
    showLogin.value = true
  }

  async function sendCode(phone: string) {
    const res = await fetch(`${API()}/api/auth/send-code`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ phone }),
    })
    return res.json()
  }

  async function login(phone: string, code: string) {
    const res = await fetch(`${API()}/api/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ phone, code }),
    })
    const data = await res.json()
    if (data.token) {
      setAuth(data.token, data.user_id)
    }
    return data
  }

  return { token, userId, showLogin, setAuth, logout, sendCode, login }
})
