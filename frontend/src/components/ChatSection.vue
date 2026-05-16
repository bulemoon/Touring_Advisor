<template>
  <div class="chat-section">
    <div class="assistant-card">
      <div class="assistant-kicker">会员专属 AI 管家</div>
      <div class="assistant-title">您好，我是鹭岛礼宾顾问</div>
      <p class="assistant-copy">
        已根据您当前所在位置，准备好景区解读、路线推荐与周边消费建议。
      </p>
      <div class="chat-input-row" @click="chat.showChat = true">
        <input
          v-model="inputText"
          class="chat-input"
          placeholder="例如：帮我安排一个鼓浪屿精华半日游"
          @click.stop
          @keyup.enter="handleSend"
        />
        <button class="chat-send-btn" @click.stop="handleSend">发送</button>
      </div>
    </div>

    <BottomSheet :visible="chat.showChat" height="70vh" @close="chat.showChat = false">
      <div class="sheet-heading">
        <div class="sheet-kicker">AI CONCIERGE</div>
        <div class="sheet-title">专属行程对话</div>
      </div>
      <div class="chat-messages" ref="msgContainer">
        <div
          v-for="(msg, i) in chat.messages"
          :key="i"
          :class="['chat-msg', msg.role === 'user' ? 'msg-user' : 'msg-assistant']"
        >
          <span v-html="formatContent(msg.content)"></span>
          <span v-if="chat.isTyping && i === chat.messages.length - 1" class="typing-cursor">|</span>
        </div>
        <div v-if="feedback" :class="['action-feedback', feedback.type]">{{ feedback.text }}</div>
      </div>
      <div class="chat-bottom-input">
        <input v-model="inputText" placeholder="输入需求，例如避开人流、偏好拍照点" @keyup.enter="handleSend" />
        <button @click="handleSend">发送</button>
      </div>
    </BottomSheet>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, nextTick } from "vue"
import { useChatStore } from "../stores/chat"
import BottomSheet from "./BottomSheet.vue"

const props = defineProps<{ lat: number; lng: number }>()

const chat = useChatStore()
const inputText = ref("")
const msgContainer = ref<HTMLElement | null>(null)
const feedback = ref<{ type: string; text: string } | null>(null)
let feedbackTimer: ReturnType<typeof setTimeout> | null = null

function formatContent(content: string): string {
  return content
    .replace(/###\s?(.+)/g, '<strong style="color:#d6b36a;font-size:15px;">$1</strong>')
    .replace(/\*\*(.+?)\*\*/g, '<strong style="color:#e8d09e;">$1</strong>')
    .replace(/\n/g, "<br/>")
}

function showFeedback(type: "cart" | "itinerary", text: string) {
  feedback.value = { type, text }
  if (feedbackTimer) clearTimeout(feedbackTimer)
  feedbackTimer = setTimeout(() => { feedback.value = null }, 3000)
}

watch(() => chat.messages.length, async () => {
  await nextTick()
  msgContainer.value?.scrollTo({ top: 9999, behavior: "smooth" })
  const last = chat.messages[chat.messages.length - 1]
  if (last?.role === "assistant") {
    if (last.content.includes("已加入购物车") || last.content.includes("已添加至购物车")) {
      showFeedback("cart", "🛒 已更新购物车")
    }
    if (last.content.includes("行程已更新") || last.content.includes("行程已生成")) {
      showFeedback("itinerary", "📋 行程已更新")
    }
  }
})

async function handleSend() {
  const text = inputText.value.trim()
  if (!text) return
  chat.showChat = true
  await chat.send(text, props.lat, props.lng)
  inputText.value = ""
}
</script>

<style scoped>
.chat-section {
  padding: 18px 16px 8px;
  background: transparent;
}

.assistant-card {
  padding: 18px;
  border-radius: 24px;
  background: linear-gradient(180deg, rgba(38, 29, 23, 0.96) 0%, rgba(22, 17, 14, 0.98) 100%);
  border: 1px solid rgba(202, 171, 104, 0.24);
  box-shadow: 0 18px 44px rgba(0, 0, 0, 0.3);
}

.assistant-kicker {
  font-size: 12px;
  letter-spacing: 0.12em;
  color: #d6b36a;
  margin-bottom: 10px;
}

.assistant-title {
  font-size: 28px;
  line-height: 1.2;
  font-weight: 700;
  color: #fff7e7;
  margin-bottom: 10px;
}

.assistant-copy {
  font-size: 15px;
  line-height: 1.7;
  color: rgba(255, 246, 228, 0.82);
  margin-bottom: 16px;
}

.chat-input-row {
  display: flex;
  gap: 10px;
  align-items: center;
  padding: 8px;
  border-radius: 999px;
  background: rgba(255, 248, 234, 0.06);
  border: 1px solid rgba(210, 180, 114, 0.16);
}

.chat-input {
  flex: 1;
  padding: 12px 14px;
  border: none;
  border-radius: 20px;
  font-size: 14px;
  outline: none;
  background: transparent;
  color: #fff4da;
}

.chat-input::placeholder {
  color: rgba(255, 241, 210, 0.45);
}

.chat-send-btn {
  padding: 12px 20px;
  border: none;
  background: linear-gradient(180deg, #d8bf79 0%, #b38a3f 100%);
  color: #2a1f12;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 700;
  white-space: nowrap;
  box-shadow: inset 0 1px 0 rgba(255, 248, 220, 0.5);
}

.sheet-heading {
  padding: 4px 0 14px;
}

.sheet-kicker {
  font-size: 11px;
  letter-spacing: 0.16em;
  color: #b99856;
  margin-bottom: 6px;
}

.sheet-title {
  font-size: 22px;
  font-weight: 700;
  color: #f6ecd7;
}

.chat-messages {
  max-height: 50vh;
  overflow-y: auto;
  padding: 8px 0;
}

.chat-msg {
  margin-bottom: 12px;
  padding: 12px 14px;
  border-radius: 16px;
  max-width: 85%;
  font-size: 14px;
  line-height: 1.6;
}

.msg-user {
  background: linear-gradient(180deg, #d7bb77 0%, #bc944d 100%);
  color: #2b2011;
  margin-left: auto;
  border-radius: 16px 16px 6px 16px;
}

.msg-assistant {
  background: rgba(57, 44, 35, 0.92);
  color: #f9f0dd;
  margin-right: auto;
  border: 1px solid rgba(201, 168, 99, 0.18);
  border-radius: 16px 16px 16px 6px;
}

.chat-bottom-input {
  display: flex;
  gap: 8px;
  padding: 12px 0;
  border-top: 1px solid rgba(194, 161, 92, 0.14);
}

.chat-bottom-input input {
  flex: 1;
  padding: 10px 14px;
  border: 1px solid rgba(197, 166, 100, 0.18);
  border-radius: 999px;
  font-size: 14px;
  outline: none;
  background: rgba(255, 248, 232, 0.04);
  color: #f7ead0;
}

.chat-bottom-input button {
  padding: 10px 20px;
  border: none;
  background: linear-gradient(180deg, #d8bf79 0%, #b38a3f 100%);
  color: #2a1f12;
  border-radius: 999px;
  font-weight: 700;
}

.typing-cursor {
  display: inline-block;
  animation: blink 0.7s infinite;
  color: #d6b36a;
  font-weight: 700;
  margin-left: 2px;
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

.action-feedback {
  text-align: center;
  padding: 6px 12px;
  margin: 6px 0;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 600;
  animation: fadeSlideIn 0.3s ease;
}

.action-feedback.cart {
  background: rgba(212, 175, 55, 0.15);
  color: #e8c86a;
  border: 1px solid rgba(212, 175, 55, 0.2);
}

.action-feedback.itinerary {
  background: rgba(76, 175, 80, 0.12);
  color: #81c784;
  border: 1px solid rgba(76, 175, 80, 0.18);
}

@keyframes fadeSlideIn {
  from { opacity: 0; transform: translateY(-8px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
