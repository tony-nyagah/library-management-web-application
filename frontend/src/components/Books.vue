<script setup lang="ts">
import useApi from "@/composables/useApi";
import stockImg from "@/assets/stock_book.jpg";

let book_route = "/books";

const { data, error, loading, load } = useApi(book_route);

load();
</script>

<template>
    <div>
        <h1 class="text-2xl font-bold underline text-center py-2">All Books</h1>
        <div v-if="loading" class="text-center py-2">Loading...</div>
        <div v-else-if="error" class="text-center py-2">An error occured: {{ error }}</div>
        <div v-else class="container mx-auto py-10 flex flex-wrap">
            <div v-for="book in data" :key="book.id" class="w-full md:w-1/2 lg:w-1/3 p-2">
                <div class="card bg-base-100 shadow-xl">
                    <figure><img :src=stockImg alt="Book" /></figure>
                    <div class="card-body">
                        <h2 class="card-title">{{ book.title }}</h2>
                        <p>Author: <strong>{{ book.author }}</strong></p>
                        <p>Available copies: {{ book.stock }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
