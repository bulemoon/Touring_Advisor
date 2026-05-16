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

export const useChatStore = defineStore("chat", () => {
  const messages = ref<ChatMessage[]>([])
  const showChat = ref(false)
  const isTyping = ref(false)
  const typingText = ref("")
  let typingTimer: ReturnType<typeof setInterval> | null = null
  let loadingDotsTimer: ReturnType<typeof setInterval> | null = null
  const loadingDots = ref("")

  // Session
  const sessionId = ref<string | null>(null)
  const sessions = ref<SessionMeta[]>([])
  const sessionState = ref<string>("")
  const currentStep = ref<string>("")

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

  function resetSession() {
    sessionId.value = null
    sessionState.value = ""
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
        showChat.value = true
      }
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
    messages.value.push({ role: "user", content: message })

    // 如果没有 session，自动创建
    if (!sessionId.value) {
      await startSession()
      // 已创建 session，再发送用户的第一条消息
      messages.value.push({ role: "user", content: message })
    }

    // 插入加载中提示
    const loadingBase = sessionState.value === "generating"
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

      // 移除加载中提示，替换为实际回复
      stopLoadingDots()
      messages.value[loadingIdx] = { role: "assistant", content: "" }
      const fullText = data.content
      typeText(fullText, (partial) => {
        messages.value[loadingIdx].content = partial
      })

      if (data.state === "done") {
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
      loadingDots.value = baseText + "·".repeat(dotCount)
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
    messages, showChat, isTyping, typingText, loadingDots,
    sessionId, sessions, sessionState, currentStep,
    send, startSession, loadSession, fetchSessions, resetSession,
    deleteSession, clearAllSessions,
    stopTyping, disconnect,
  }
})
