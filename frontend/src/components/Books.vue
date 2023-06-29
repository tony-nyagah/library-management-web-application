<template>
    <div class="p-6">
        <h1 class="text-3xl mb-4">Books</h1>
        <div v-if="loading">
            Loading...
        </div>
        <div v-else>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <div v-for="book in data" :key="book.id" class="rounded overflow-hidden shadow-lg p-6 bg-white">
                    <div class="font-bold text-xl mb-2">{{ book.title }}</div>
                    <p class="text-gray-700 text-base">
                        {{ book.author }}
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import useApi from '../composables/useApi'

const { data, error, loading, load } = useApi('books')

onMounted(async () => {
    await load()
    if (error.value) {
        console.error(error.value)
    }
})
</script>
