<script setup lang="ts">
import { onMounted, ref } from 'vue'
import useApi from '../composables/useApi'
import { useRoute } from 'vue-router'

const route = useRoute()
const data = ref(null)
const error = ref(null)
const loading = ref(false)
let load = null;

onMounted(async () => {
    if (route.params.id) {
        const api = useApi(`books/${route.params.id}`);
        data.value = api.data;
        error.value = api.error;
        loading.value = api.loading;
        load = api.load;
        await load()
        if (error.value) {
            console.error(error.value)
        }
    }
})
</script>

<template>
    <div class="p-6" v-if="loading">
        Loading...
    </div>
    <div class="p-6" v-else>
        <h1 class="text-3xl mb-4">{{ data.title }}</h1>
        <p class="text-gray-700 text-base">
            {{ data.author }}
        </p>
        <!-- Add any other book details you want to display here -->
    </div>
</template>
