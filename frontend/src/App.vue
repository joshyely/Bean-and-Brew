<script setup>
import { ref } from 'vue';
import Navbar from './components/nav/Navbar.vue'
import { apiTestCall } from './utils/axiosAPI.js'
import { saveToken, getToken, deleteToken } from './utils/auth.js'

const count = ref(0);
</script>

<template>
<header>
  <Navbar />
</header>
<main>
  <RouterView />
</main>
</template>


<style>

</style>