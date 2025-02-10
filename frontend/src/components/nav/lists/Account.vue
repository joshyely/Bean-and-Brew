<script setup>
import { ref } from 'vue';
const loggedIn = ref(false);
</script>

<template>
<ul id="account-nav" class="nav-list" v-if="!loggedIn">
    <li class="nav-item">
        <RouterLink to="/login">Login</RouterLink>
    </li>
    <li class="nav-item">
        <RouterLink to="/register">Register</RouterLink>
    </li>
</ul>
<ul id="account-nav" class="nav-list" v-else>
    <li class="nav-item">
        <RouterLink to="/profile">Profile</RouterLink>
    </li>
    <li class="nav-item">
        <RouterLink to="/logout">Logout</RouterLink>
    </li>
</ul>
</template>