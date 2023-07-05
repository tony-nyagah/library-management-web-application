<script setup lang="ts">
import { onMounted } from "vue";
import useApi from "../composables/useApi";

const { data, error, loading, load } = useApi("books");

onMounted(async () => {
    await load()
    if (error.value) {
        console.error(error.value)
    } else {
        console.log(data.value)
    }
})
</script>

<template>
    <div class="container mx-auto px-5">
        <div class="grid grid-cols-10">
            <div class="col-span-10 sm:col-span-8">
                <h1 class="text-2xl font-bold">Books</h1>
                <hr class="my-4">
                <button type="button" class="btn btn-success btn-sm text-white">Add Book</button>
                <hr class="my-4">
                <table class="table-auto w-full">
                    <thead class="">
                        <tr>
                            <th>Title</th>
                            <th>Author</th>
                            <th>Available Copies</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="text-center">foo</td>
                            <td class="text-center">bar</td>
                            <td class="text-center">20</td>
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
