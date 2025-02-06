<script setup>

import Navbar from './components/Navbar.vue'
import { apiTestCall } from './utils/axiosAPI.js'
import { saveToken, getToken, deleteToken } from './utils/auth.js'

</script>

<template>
  <header>
    <Navbar/>
  </header>
  <main>
    <RouterView />
  </main>
</template>

<style scoped>

</style>