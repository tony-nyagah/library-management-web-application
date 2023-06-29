<script setup lang="ts">
import useApi from "@/composables/useApi";

let book_route = "/books";

const { data, error, loading, load } = useApi(book_route);

load();
</script>

<template>
    <div>
        <h1>Books</h1>
        <div v-if="loading">Loading...</div>
        <div v-else-if="error">An error occured: {{ error }}</div>
        <div v-else>
            <ul>
                <li v-for="book in data" :key="book.id">
                    <h2>{{ book.title }}</h2>
                    <p>{{ book.author }}</p>
                </li>
            </ul>
        </div>
    </div>
</template>
