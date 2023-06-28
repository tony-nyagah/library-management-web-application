<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";

let ping_message = ref("");

function ping_server() {
    axios.get("http://localhost:5000/ping").then((response) => {
        ping_message.value = response.data;
    })
}

onMounted(() => {
    ping_server();
})

</script>

<template>
    <h1>{{ ping_message }}</h1>
</template>
