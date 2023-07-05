<script setup lang="ts">
import { ref, onMounted } from 'vue'

defineProps<{
  msg: string
}>()

let ping_message = ref('')

async function ping_server() {
  const response = await fetch('http://localhost:5001/ping')
  const data = await response.json()
  ping_message.value = data
  console.log(data)
}

onMounted(() => {
  ping_server()
})
</script>

<template>
  <h1>
    {{ msg }} <span class="underline font-bold">{{ ping_message }}</span>
  </h1>
</template>
