import { defineStore } from "pinia"
import { ref } from "vue"

interface ChatMessage {
  role: "user" | "assistant"
  content: string
}

export const useChatStore = defineStore("chat", () => {
  const messages = ref<ChatMessage[]>([])
  const showChat = ref(false)
  const isTyping = ref(false)
  const typingText = ref("")
  let typingTimer: ReturnType<typeof setInterval> | null = null

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

  async function send(message: string, lat: number, lng: number) {
    messages.value.push({ role: "user", content: message })
    try {
      const res = await fetch(`${API()}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, lat, lng }),
      })
      const data = await res.json()
      const fullText = data.content
      messages.value.push({ role: "assistant", content: "" })
      const lastIdx = messages.value.length - 1
      typeText(fullText, (partial) => {
        messages.value[lastIdx].content = partial
      })
    } catch {
      messages.value.push({ role: "assistant", content: "网络异常，请稍后重试" })
    }
  }

  function stopTyping() {
    if (typingTimer) {
      clearInterval(typingTimer)
      typingTimer = null
    }
    isTyping.value = false
    typingText.value = ""
    const last = messages.value[messages.value.length - 1]
    if (last && last.role === "assistant" && !last.content) {
      messages.value.pop()
    }
  }

  function disconnect() {
    stopTyping()
  }

  return { messages, showChat, isTyping, typingText, send, stopTyping, disconnect }
})
