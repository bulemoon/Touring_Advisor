<template>
  <Teleport to="body">
    <div v-if="visible" class="bottom-sheet-overlay" @click.self="$emit('close')">
      <div class="bottom-sheet" :style="{ height }">
        <div class="bottom-sheet-handle" />
        <div class="bottom-sheet-content">
          <slot />
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
defineProps<{ visible: boolean; height?: string }>()
defineEmits<{ close: [] }>()
</script>

<style scoped>
.bottom-sheet-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
  z-index: 1000;
  display: flex;
  align-items: flex-end;
  backdrop-filter: blur(10px);
}

.bottom-sheet {
  background: linear-gradient(180deg, rgba(34, 27, 22, 0.98) 0%, rgba(15, 12, 10, 1) 100%);
  border-radius: 24px 24px 0 0;
  width: 100%;
  overflow-y: auto;
  animation: slideUp 0.3s ease;
  border-top: 1px solid rgba(203, 171, 104, 0.2);
  color: #f7ecd7;
}

.bottom-sheet-handle {
  width: 40px;
  height: 4px;
  background: rgba(224, 193, 122, 0.38);
  border-radius: 2px;
  margin: 12px auto 8px;
}

.bottom-sheet-content {
  padding: 0 16px 24px;
}

@keyframes slideUp {
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
}
</style>
