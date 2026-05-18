import { defineStore } from "pinia"
import { ref } from "vue"

interface ChatMessage {
  role: "user" | "assistant"
  content: string
}

interface SessionMeta {
  session_id: string
  destination: string | null
  duration: string | null
  created_at: string
  message_count: number
}

export interface RouteStop {
  name: string
  address?: string
  lat: number
  lng: number
  sort_order?: number
  duration_minutes?: number
  tip?: string
}

export interface RouteSegment {
  from?: string
  to?: string
  distance_m?: number
  duration_sec?: number
  polyline?: [number, number][]
  source?: string
}

export interface RouteDay {
  day: number
  stops: RouteStop[]
  segments?: RouteSegment[]
  polyline?: [number, number][]
  distance_m?: number
  travel_duration_sec?: number
  stay_duration_min?: number
}

export interface RoutePlan {
  title?: string
  summary?: string
  coord_system?: string
  mode?: string
  optimized?: boolean
  start?: RouteStop | null
  days?: RouteDay[]
  stops?: RouteStop[]
  polyline?: [number, number][]
  distance_m?: number
  travel_duration_sec?: number
}

export interface ShoppingRecommendation {
  name: string
  type?: string
  address?: string
  distance?: string | number
  distance_m?: number
  lat?: number | null
  lng?: number | null
  rating?: string | number
  reason?: string
  source?: "itinerary_product" | "souvenir" | "local_shop" | "nearby"
  purchase_keywords?: string[]
  recommended_products?: string[]
}

export const useChatStore = defineStore("chat", () => {
  const messages = ref<ChatMessage[]>([])
  const showChat = ref(false)
  const isTyping = ref(false)
  const typingText = ref("")
  let typingTimer: ReturnType<typeof setInterval> | null = null
  let loadingDotsTimer: ReturnType<typeof setInterval> | null = null
  const loadingDots = ref("")

  const sessionId = ref<string | null>(null)
  const sessions = ref<SessionMeta[]>([])
  const sessionState = ref<string>("")
  const currentStep = ref<string>("")
  const currentRoutePlan = ref<RoutePlan | null>(null)
  const currentShoppingRecommendations = ref<ShoppingRecommendation[]>([])

  const API = () => window.CONFIG?.API_BASE_URL || ""

  function typeText(fullText: string, onChar: (partial: string) => void) {
    let i = 0
    typingText.value = ""
    isTyping.value = true
    const speed = 25
    typingTimer = setInterval(() => {
      i++
      const partial = fullText.slice(0, i)
      typingText.value = partial
      onChar(partial)
      if (i >= fullText.length) {
        clearInterval(typingTimer!)
        typingTimer = null
        isTyping.value = false
        typingText.value = ""
      }
    }, speed)
  }

  function getShoppingFromSession(data: any): ShoppingRecommendation[] {
    const shopping = data?.shopping || data?.result?.shopping || []
    return Array.isArray(shopping) ? shopping : []
  }

  function syncFromPayload(data: any) {
    currentRoutePlan.value = data?.route_plan || data?.result?.route_plan || currentRoutePlan.value
    const shopping = getShoppingFromSession(data)
    if (Object.prototype.hasOwnProperty.call(data || {}, "shopping") || Object.prototype.hasOwnProperty.call(data?.result || {}, "shopping")) {
      currentShoppingRecommendations.value = shopping
    }
  }

  function resetSession() {
    sessionId.value = null
    sessionState.value = ""
    currentRoutePlan.value = null
    currentShoppingRecommendations.value = []
    messages.value = []
    stopTyping()
  }

  async function startSession(): Promise<string> {
    const res = await fetch(`${API()}/api/session/start`, { method: "POST" })
    const data = await res.json()
    sessionId.value = data.session_id
    sessionState.value = "collecting"
    currentStep.value = data.current_step || "destination"
    messages.value = [{ role: "assistant", content: data.message }]
    showChat.value = true
    await fetchSessions()
    return data.session_id
  }

  async function fetchSessions() {
    try {
      const res = await fetch(`${API()}/api/session/list`)
      if (!res.ok) {
        console.error("[Chat] fetchSessions failed:", res.status, res.statusText)
        return
      }
      const data = await res.json()
      sessions.value = data
      console.log("[Chat] fetched sessions:", data.length)
    } catch (e) {
      console.error("[Chat] fetchSessions error:", e)
    }
  }

  async function loadSession(sid: string) {
    try {
      const res = await fetch(`${API()}/api/session/${sid}`)
      const data = await res.json()
      if (data.messages) {
        messages.value = data.messages
        sessionId.value = sid
        sessionState.value = data.state || "done"
        currentStep.value = data.current_step || ""
        currentRoutePlan.value = data.route_plan || data.result?.route_plan || null
        currentShoppingRecommendations.value = getShoppingFromSession(data)
        showChat.value = true
      }
    } catch {}
  }

  async function syncCurrentRoutePlan() {
    if (!sessionId.value) return
    try {
      const res = await fetch(`${API()}/api/session/${sessionId.value}`)
      if (!res.ok) return
      const data = await res.json()
      syncFromPayload(data)
    } catch {}
  }

  async function deleteSession(sid: string) {
    try {
      await fetch(`${API()}/api/session/${sid}`, { method: "DELETE" })
      sessions.value = sessions.value.filter(s => s.session_id !== sid)
      if (sessionId.value === sid) {
        resetSession()
      }
    } catch {}
  }

  async function clearAllSessions() {
    try {
      const res = await fetch(`${API()}/api/session/all`, { method: "DELETE" })
      if (!res.ok) {
        console.error("[Chat] clearAllSessions failed:", res.status)
        return
      }
      sessions.value = []
      resetSession()
      console.log("[Chat] all sessions cleared")
    } catch (e) {
      console.error("[Chat] clearAllSessions error:", e)
    }
  }

  async function send(message: string, lat: number, lng: number) {
    const isConfirmingGeneration = sessionState.value === "confirming" && /^(确认|好的|可以|没问题|ok|yes|对|没错)$/i.test(message.trim())
    if (isConfirmingGeneration) {
      messages.value = [{ role: "user", content: message }]
    } else {
      messages.value.push({ role: "user", content: message })
    }

    if (!sessionId.value) {
      await startSession()
      messages.value.push({ role: "user", content: message })
    }

    const loadingBase = sessionState.value === "generating" || isConfirmingGeneration
      ? "正在生成推荐方案"
      : "正在查询天气与周边信息"
    const loadingIdx = messages.value.length
    messages.value.push({ role: "assistant", content: loadingBase + "..." })
    startLoadingDots(loadingBase)

    try {
      const res = await fetch(`${API()}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message,
          lat,
          lng,
          session_id: sessionId.value,
        }),
      })
      const data = await res.json()

      if (data.session_id) {
        sessionId.value = data.session_id
        sessionState.value = data.state || sessionState.value
        currentStep.value = data.current_step || currentStep.value
      }
      syncFromPayload(data)

      stopLoadingDots()
      messages.value[loadingIdx] = { role: "assistant", content: "" }
      const fullText = data.content
      typeText(fullText, (partial) => {
        messages.value[loadingIdx].content = partial
      })

      if (data.state === "done") {
        if ((!data.route_plan && !data.result?.route_plan) || !getShoppingFromSession(data).length) {
          await syncCurrentRoutePlan()
        }
        await fetchSessions()
      }
    } catch {
      stopLoadingDots()
      messages.value[loadingIdx] = { role: "assistant", content: "网络异常，请稍后重试" }
    }
  }

  function startLoadingDots(baseText: string) {
    let dotCount = 0
    loadingDots.value = baseText
    loadingDotsTimer = setInterval(() => {
      dotCount = (dotCount + 1) % 4
      loadingDots.value = baseText + ".".repeat(dotCount)
    }, 500)
  }

  function stopLoadingDots() {
    if (loadingDotsTimer) {
      clearInterval(loadingDotsTimer)
      loadingDotsTimer = null
    }
    loadingDots.value = ""
  }

  function stopTyping() {
    if (typingTimer) {
      clearInterval(typingTimer)
      typingTimer = null
    }
    isTyping.value = false
    typingText.value = ""
    stopLoadingDots()
    const last = messages.value[messages.value.length - 1]
    if (last && last.role === "assistant" && !last.content) {
      messages.value.pop()
    }
  }

  function disconnect() {
    stopTyping()
  }

  return {
    messages,
    showChat,
    isTyping,
    typingText,
    loadingDots,
    sessionId,
    sessions,
    sessionState,
    currentStep,
    currentRoutePlan,
    currentShoppingRecommendations,
    send,
    startSession,
    loadSession,
    fetchSessions,
    resetSession,
    deleteSession,
    clearAllSessions,
    stopTyping,
    disconnect,
  }
})
