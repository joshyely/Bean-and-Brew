<script setup>
import { ref, onMounted } from 'vue';
import Navbar from './components/nav/Navbar.vue'
import FooterComp from './components/Footer.vue'
import { apiTest } from './utils/axiosAPI.js'
import { saveToken, getToken, deleteToken } from '@/utils/auth.js'
import { mobile } from '@/utils/responsive.js'

onMounted(() => {
  apiTest();
});

</script>

<template>
<header>
  <Navbar />
</header>
<div class="main-wrapper">
  <main :class="[!!mobile && 'mobile']">
    <RouterView />
  </main>
</div>

<footer>
  <FooterComp />
</footer>
</template>

<style lang="scss">

</style>