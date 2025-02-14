<script setup>
import { ref } from 'vue'
import ShowIcon from '../components/icons/Show.vue'
import HideIcon from '../components/icons/Hide.vue'

const passwordShow = ref(false);

const submit = () => {

}


</script>


<template>
<div class="wrapper">
<section class="account">
    <h1>Login</h1>
    <br>
    <form @submit="">
        <div class="field">
            <input type="email" placeholder="Email" required>
        </div>
        <div class="field password">
            <input :type="[!passwordShow ? 'password' : 'text' ]" placeholder="Password" required>
            <span class="show-toggle-btn">
                <ShowIcon @click="() => passwordShow = false" v-if="passwordShow"/>
                <HideIcon @click="() => passwordShow = true" v-else/>
            </span>
        </div>
        <input type="submit" value="Login">
        <p>Don't have an account? <RouterLink to="/register">Register here</RouterLink></p>
    </form>
</section>
</div>

</template>

<style scoped lang="scss">


</style>