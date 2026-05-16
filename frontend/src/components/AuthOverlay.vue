<template>
  <div v-if="visible" class="auth-overlay">
    <div class="auth-card">
      <h2>欢迎使用 AI 旅伴助手</h2>
      <p class="auth-subtitle">登录后即可享受个性化旅行服务</p>
      <input v-model="phone" type="tel" placeholder="手机号" class="auth-input" maxlength="11" />
      <div class="code-row">
        <input v-model="code" type="text" placeholder="验证码" class="auth-input code-input" maxlength="6" />
        <button class="code-btn" :disabled="countdown > 0" @click="handleSendCode">
          {{ countdown > 0 ? `${countdown}s` : "获取验证码" }}
        </button>
      </div>
      <button class="login-btn" @click="handleLogin">登录 / 注册</button>
      <p v-if="error" class="auth-error">{{ error }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue"
import { useAuthStore } from "../stores/auth"

defineProps<{ visible: boolean }>()

const auth = useAuthStore()
const phone = ref("")
const code = ref("")
const countdown = ref(0)
const error = ref("")
let timer: ReturnType<typeof setInterval> | null = null

async function handleSendCode() {
  if (phone.value.length < 11) return
  error.value = ""
  await auth.sendCode(phone.value)
  countdown.value = 60
  if (timer) clearInterval(timer)
  timer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0 && timer) clearInterval(timer)
  }, 1000)
}

async function handleLogin() {
  error.value = ""
  const res = await auth.login(phone.value, code.value)
  if (!res.token) {
    error.value = res.detail || "登录失败"
  }
}
</script>

<style scoped>
.auth-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(8px);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
}
.auth-card {
  background: #fff;
  border-radius: 20px;
  padding: 32px 24px;
  width: 85%;
  max-width: 360px;
}
.auth-card h2 { margin: 0 0 8px; font-size: 22px; text-align: center; }
.auth-subtitle { color: #888; text-align: center; margin-bottom: 24px; font-size: 14px; }
.auth-input {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 16px;
  margin-bottom: 12px;
  box-sizing: border-box;
}
.code-row { display: flex; gap: 8px; }
.code-input { flex: 1; }
.code-btn {
  padding: 12px 16px;
  border: none;
  background: #4CAF50;
  color: #fff;
  border-radius: 10px;
  white-space: nowrap;
  font-size: 14px;
}
.code-btn:disabled { background: #ccc; }
.login-btn {
  width: 100%;
  padding: 14px;
  border: none;
  background: #4CAF50;
  color: #fff;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  margin-top: 8px;
}
.auth-error { color: #e53935; text-align: center; margin-top: 8px; font-size: 13px; }
</style>
