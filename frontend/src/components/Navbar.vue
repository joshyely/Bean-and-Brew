<script setup>
import Logo from './Logo.vue'
</script>

<template>
<div class="wrapper">
    <RouterLink to="/"><Logo/></RouterLink>
    <nav>
        <RouterLink to="/">About</RouterLink>
        <RouterLink to="/">Contact</RouterLink>
    </nav>
</div>
</template>


<style scoped>


@media(min-width: 800px){
    .wrapper{
        padding: 0 1%;
        display:flex;
        align-items: center;
    } 
}
</style>