<script setup>
import { ref, onMounted } from 'vue';
import Navbar from './components/nav/Navbar.vue'
import FooterComp from './components/Footer.vue'
import { apiTestCall } from './utils/axiosAPI.js'
import { saveToken, getToken, deleteToken } from '@/utils/auth.js'
import { mobile } from '@/utils/responsive.js'
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
.main-wrapper{
  display:flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
}
main{
  width:100%;
  section {
    margin: 0 auto;
    padding: 3%;
    min-height: fit-content;
    h1{
      font-size: 2.1em;
    }
  }
}
</style>