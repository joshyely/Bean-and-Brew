<script setup>
import { ref } from 'vue';
import Navbar from './components/nav/Navbar.vue'
import FooterComp from './components/Footer.vue'
import { apiTestCall } from './utils/axiosAPI.js'
import { saveToken, getToken, deleteToken } from './utils/auth.js'


</script>

<template>
<header>
  <Navbar />
</header>
<main>
  <RouterView />
</main>
<footer>
  <FooterComp />
</footer>
</template>