<template>
  <div class="chat-section">
    <div class="assistant-card">
      <div class="assistant-kicker">会员专属 AI 管家</div>
      <div class="assistant-title">您好，我是旅行顾问</div>
      <p class="assistant-copy">
        已根据您当前所在位置，准备好景区解读、路线推荐与周边消费建议。
      </p>
      <div class="chat-input-row" @click="chat.showChat = true">
        <input
          v-model="inputText"
          class="chat-input"
          placeholder="例如：帮我安排一个鼓浪屿精华半日游"
          @click.stop
          @keyup.enter="handleNewSession"
        />
        <button class="chat-send-btn" @click.stop="handleNewSession">发送</button>
      </div>
      <div class="history-row" ref="historyDropdownRef">
        <div class="history-dropdown-trigger" @click="toggleHistoryDropdown">
          <span>历史会话记录</span>
          <span v-if="chat.sessions.length > 0" class="history-badge">{{ chat.sessions.length }}</span>
          <span class="history-arrow" :class="{ open: showHistoryDropdown }">▼</span>
        </div>

        <div v-if="showHistoryDropdown" class="history-dropdown-panel">
          <div v-if="chat.sessions.length === 0" class="history-empty">暂无历史会话</div>
          <div
            v-for="s in chat.sessions"
            :key="s.session_id"
            class="history-item"
            :class="{ active: selectedSessionId === s.session_id }"
          >
            <div class="history-item-label" @click="loadSession(s.session_id)">
              {{ formatSessionLabel(s) }}
            </div>
            <button
              class="history-item-delete"
              @click.stop="deleteOne(s.session_id)"
              title="删除"
            >
              ×
            </button>
          </div>
          <div v-if="chat.sessions.length > 0" class="history-dropdown-footer">
            <button class="history-btn danger" @click="clearAll">清空全部</button>
          </div>
        </div>
      </div>
    </div>

    <BottomSheet :visible="chat.showChat" height="70vh" @close="chat.showChat = false">
      <div class="sheet-heading">
        <div class="sheet-kicker">AI CONCIERGE</div>
        <div class="sheet-title-row">
          <div class="sheet-title">专属行程对话</div>
          <div class="history-select-wrapper">
            <select
              class="history-select"
              v-model="selectedSessionId"
              @change="onHistorySelect"
            >
              <option value="">当前对话</option>
              <option
                v-for="s in chat.sessions"
                :key="s.session_id"
                :value="s.session_id"
              >
                {{ formatSessionLabel(s) }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="chat-messages" ref="msgContainer">
        <div
          v-for="(msg, i) in chat.messages"
          :key="i"
          :class="['chat-msg', msg.role === 'user' ? 'msg-user' : 'msg-assistant', { 'msg-loading': isLoadingMsg(msg.content) }]"
        >
          <span
            v-if="isLoadingMsg(msg.content)"
            class="loading-text"
            v-html="chat.loadingDots"
          ></span>
          <span v-else v-html="formatContent(msg.content)"></span>
          <span v-if="chat.isTyping && i === chat.messages.length - 1" class="typing-cursor">|</span>
        </div>
        <div v-if="feedback" :class="['action-feedback', feedback.type]">{{ feedback.text }}</div>
      </div>
      <div class="chat-bottom-input">
        <template v-if="isDateStep">
          <input
            type="date"
            v-model="selectedDate"
            ref="dateInputRef"
            class="date-picker"
            @click="openDatePicker"
          />
          <button @click="handleDateSubmit">确认日期</button>
        </template>
        <template v-else>
          <input v-model="inputText" placeholder="输入需求，例如避开人流、偏好拍照点" @keyup.enter="handleSend" />
          <button @click="handleSend">发送</button>
        </template>
      </div>
    </BottomSheet>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, nextTick, onMounted, onBeforeUnmount } from "vue"
import { useChatStore } from "../stores/chat"
import BottomSheet from "./BottomSheet.vue"

const props = defineProps<{ lat: number; lng: number }>()

const chat = useChatStore()
const inputText = ref("")
const msgContainer = ref<HTMLElement | null>(null)
const feedback = ref<{ type: string; text: string } | null>(null)
let feedbackTimer: ReturnType<typeof setTimeout> | null = null

const selectedSessionId = ref("")
const showHistoryDropdown = ref(false)
const historyDropdownRef = ref<HTMLElement | null>(null)
const dateInputRef = ref<HTMLInputElement | null>(null)

// Date picker
const selectedDate = ref("")
const isDateStep = ref(false)

watch(() => chat.currentStep, (step) => {
  isDateStep.value = step === "date"
  if (isDateStep.value) {
    // Set default to today
    const today = new Date()
    selectedDate.value = today.toISOString().split('T')[0]
  }
}, { immediate: true })

onMounted(() => {
  chat.fetchSessions()
  document.addEventListener("click", onClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener("click", onClickOutside)
})

function onClickOutside(e: MouseEvent) {
  if (historyDropdownRef.value && !historyDropdownRef.value.contains(e.target as Node)) {
    showHistoryDropdown.value = false
  }
}

function toggleHistoryDropdown() {
  showHistoryDropdown.value = !showHistoryDropdown.value
}

function formatSessionLabel(s: { destination: string | null; duration: string | null; created_at: string }): string {
  const parts: string[] = []
  if (s.destination) parts.push(s.destination)
  if (s.duration) parts.push(s.duration)
  if (parts.length === 0) {
    const d = new Date(s.created_at)
    parts.push(d.toLocaleDateString("zh-CN"))
  }
  return parts.join(" · ")
}

function onHistorySelect() {
  if (selectedSessionId.value) {
    chat.loadSession(selectedSessionId.value)
  }
}

async function loadSession(sid: string) {
  selectedSessionId.value = sid
  showHistoryDropdown.value = false
  await chat.loadSession(sid)
}

async function deleteOne(sid: string) {
  if (!confirm("确定删除该会话吗？")) {
    return
  }
  await chat.deleteSession(sid)
  if (selectedSessionId.value === sid) {
    selectedSessionId.value = ""
  }
  showFeedback("itinerary", "🗑️ 会话已删除")
}

async function clearAll() {
  if (!confirm("确定要清空所有历史会话吗？此操作不可恢复。")) {
    return
  }
  await chat.clearAllSessions()
  selectedSessionId.value = ""
  showHistoryDropdown.value = false
  showFeedback("itinerary", "🗑️ 历史会话已清空")
}

watch(() => chat.sessionId, () => {
  selectedSessionId.value = chat.sessionId || ""
})

function isLoadingMsg(content: string): boolean {
  return content.startsWith("正在")
}

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

async function handleNewSession() {
  const text = inputText.value.trim()
  if (!text) return
  chat.resetSession()
  chat.showChat = true
  await chat.send(text, props.lat, props.lng)
  inputText.value = ""
}

async function handleSend() {
  const text = inputText.value.trim()
  if (!text) return
  chat.showChat = true
  await chat.send(text, props.lat, props.lng)
  inputText.value = ""
}

async function handleDateSubmit() {
  if (!selectedDate.value) return
  // Format date as "5月20日" in Chinese
  const d = new Date(selectedDate.value)
  const month = d.getMonth() + 1
  const day = d.getDate()
  const formattedDate = `${month}月${day}日`
  
  chat.showChat = true
  await chat.send(formattedDate, props.lat, props.lng)
  selectedDate.value = ""
}

function openDatePicker() {
  const el = dateInputRef.value as HTMLInputElement & { showPicker?: () => void }
  if (!el) return
  if (typeof el.showPicker === "function") {
    el.showPicker()
  } else {
    el.focus()
  }
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

.chat-input.date-picker {
  color-scheme: dark;
  cursor: pointer;
}

.chat-input.date-picker::-webkit-calendar-picker-indicator {
  filter: invert(1);
  opacity: 0.6;
  cursor: pointer;
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
  cursor: pointer;
}

.history-row {
  position: relative;
  padding: 8px;
  margin-top: 10px;
  border-radius: 999px;
  background: rgba(255, 248, 234, 0.06);
  border: 1px solid rgba(210, 180, 114, 0.16);
}

.history-dropdown-trigger {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  cursor: pointer;
  color: #d6b36a;
  font-size: 13px;
  user-select: none;
}

.history-dropdown-trigger span:first-child {
  flex: 1;
}

.history-badge {
  background: linear-gradient(180deg, #d8bf79 0%, #b38a3f 100%);
  color: #2a1f12;
  font-size: 11px;
  font-weight: 700;
  padding: 1px 6px;
  border-radius: 999px;
  min-width: 18px;
  text-align: center;
}

.history-arrow {
  font-size: 10px;
  color: rgba(214, 179, 106, 0.6);
  transition: transform 0.2s ease;
}

.history-arrow.open {
  transform: rotate(180deg);
}

.history-dropdown-panel {
  position: absolute;
  top: calc(100% + 6px);
  left: 0;
  right: 0;
  z-index: 200;
  background: linear-gradient(180deg, rgba(38, 29, 23, 0.98) 0%, rgba(22, 17, 14, 0.99) 100%);
  border: 1px solid rgba(201, 168, 99, 0.22);
  border-radius: 16px;
  padding: 6px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
  max-height: 260px;
  overflow-y: auto;
}

.history-empty {
  padding: 16px;
  text-align: center;
  color: rgba(214, 179, 106, 0.5);
  font-size: 13px;
}

.history-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  border-radius: 12px;
  cursor: pointer;
  transition: background 0.15s ease;
}

.history-item:hover {
  background: rgba(210, 180, 114, 0.1);
}

.history-item.active {
  background: rgba(210, 180, 114, 0.15);
}

.history-item-label {
  flex: 1;
  font-size: 13px;
  color: #f7ead0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.history-item-delete {
  padding: 4px 10px;
  border: none;
  border-radius: 8px;
  background: rgba(192, 57, 43, 0.15);
  color: #e57373;
  font-size: 16px;
  line-height: 1;
  cursor: pointer;
  transition: background 0.15s ease;
}

.history-item-delete:hover {
  background: rgba(192, 57, 43, 0.3);
}

.history-dropdown-footer {
  display: flex;
  justify-content: flex-end;
  padding: 8px 6px 4px;
  border-top: 1px solid rgba(201, 168, 99, 0.12);
  margin-top: 4px;
}

.history-btn {
  padding: 8px 16px;
  border: none;
  border-radius: 999px;
  background: linear-gradient(180deg, #d8bf79 0%, #b38a3f 100%);
  color: #2a1f12;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  box-shadow: inset 0 1px 0 rgba(255, 248, 220, 0.5);
}

.history-btn.danger {
  background: linear-gradient(180deg, #c0392b 0%, #922b21 100%);
  color: #fff;
  box-shadow: inset 0 1px 0 rgba(255, 150, 140, 0.4);
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

.sheet-title-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.sheet-title {
  font-size: 22px;
  font-weight: 700;
  color: #f6ecd7;
  white-space: nowrap;
}

.history-select-wrapper {
  flex: 1;
  max-width: 160px;
}

.history-select {
  width: 100%;
  padding: 6px 10px;
  border: 1px solid rgba(197, 166, 100, 0.25);
  border-radius: 10px;
  background: rgba(57, 44, 35, 0.85);
  color: #d6b36a;
  font-size: 12px;
  outline: none;
  cursor: pointer;
  appearance: auto;
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

.msg-loading {
  opacity: 0.7;
  font-style: italic;
}

.loading-text {
  animation: pulse 1.2s infinite;
  display: inline-block;
}

@keyframes pulse {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 1; }
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

.chat-bottom-input input.date-picker {
  color-scheme: dark;
  cursor: pointer;
}

.chat-bottom-input input.date-picker::-webkit-calendar-picker-indicator {
  filter: invert(1);
  opacity: 0.6;
  cursor: pointer;
}

.chat-bottom-input button {
  padding: 10px 20px;
  border: none;
  background: linear-gradient(180deg, #d8bf79 0%, #b38a3f 100%);
  color: #2a1f12;
  border-radius: 999px;
  font-weight: 700;
  cursor: pointer;
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
