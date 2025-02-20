<script setup>
import { loggedIn, logout } from '@/utils/auth';

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
        <a @click="logout">Logout</a>
    </li>
</ul>
</template>