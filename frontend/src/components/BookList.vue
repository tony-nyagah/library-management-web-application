<script setup lang="ts">
import { onMounted } from 'vue'
import useApi from '../composables/useApi'

const { data, error, loading, load } = useApi('books')

onMounted(async () => {
    await load()
    if (error.value) {
        console.error(error.value)
    }
})

const book_data = data;

</script>

<template>
    <div class="container mx-auto px-5">
        <div class="grid grid-cols-10">
            <div class="col-span-10 sm:col-span-8">
                <h1 class="text-2xl font-bold">Books</h1>
                <hr class="my-4" />
                <button type="button" class="btn btn-success btn-sm text-white">Add Book</button>
                <hr class="my-4" />
                <div v-if="loading">
                    Loading...
                </div>

                <table class="table text-xl">
                    <thead class="text-xl">
                        <tr>
                            <th>Title</th>
                            <th>Author</th>
                            <th>Available Copies</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="book in book_data" :key="book.id">
                            <td>{{ book.title }}</td>
                            <td>{{ book.author }}</td>
                            <td>{{ book.available_copies }}</td>
                            <td>
                                <div class="btn-group">
                                    <button type="button" class="btn btn-warning btn-sm">Update</button>
                                    <button type="button" class="btn btn-error btn-sm">Delete</button>
                                </div>
                            </td>
                        </tr>

                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
