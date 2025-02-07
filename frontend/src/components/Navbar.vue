<script setup>
import Logo from './Logo.vue'
import Theme from './Theme.vue';
</script>

<template>
<div class="wrapper">
    <RouterLink to="/"><Logo/></RouterLink>
    <nav>
        <RouterLink to="/">About</RouterLink>
        <RouterLink to="/">Contact</RouterLink>
    </nav>
    <Theme />
</div>
</template>


<style scoped>

.wrapper{
    background-color: rgb(50, 50, 50);
}

@media(min-width: 800px){
    .wrapper{
        padding: 0 1%;
        display:flex;
        align-items: center;
    } 
}
</style>