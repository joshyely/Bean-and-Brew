<script setup>
import { ref, onMounted, watch } from 'vue';
import Navbar from './components/nav/Navbar.vue'
import FooterComp from './components/Footer.vue'
import { apiTest } from './utils/axiosAPI.js'
import { saveToken, getToken, deleteToken } from '@/utils/auth.js'
import { mobile } from '@/utils/responsive.js'


const apiError = ref(false);
const showApiError = ref(false);
watch(()=>apiError.value, (err)=>{
  if(err){
    showApiError.value = true;
    setTimeout(()=>showApiError.value=false, 5000)
  } else {
    showApiError.value = false;
  }
});


const testAPI = async () => {
  apiError.value = await apiTest();;
}
testAPI()
</script>

<template>
  <div class="wrapper">
    <header>
      <Navbar />
    </header>
    <div class="main-wrapper">
      <main :class="[!!mobile && 'mobile']">
        <RouterView />
      </main>
      <transition name="api-transition">
        <div class="api-error" v-if="showApiError">
          <p>Couldn't connect to API</p>
        </div>
      </transition>
    </div>

    <footer>
      <FooterComp />
    </footer>
  </div>
</template>

<style lang="scss">
.api-error {
  position: sticky;
  background-color: rgb(49, 49, 49);
  border-radius: 25px;
  bottom: 5%;
  left: 25%;
  width: 50%;
  padding: 20px 20px;
  margin-bottom: 3vh;
  p {
    color: white;
  }
}

.api-transition-enter-active,
.api-transition-leave-active {
  transition: opacity 0.5s ease;
}

.api-transition-enter-from,
.api-transition-leave-to {
  opacity: 0;
}
</style>