<script setup>
import { ref } from 'vue';
import DarkTheme from './icons/DarkTheme.vue';
import LightTheme from './icons/LightTheme.vue';

const docElem = document.documentElement;
var theme = ref('light');

const getSavedTheme = () => {
    let localTheme = localStorage.getItem('theme');
    if (localTheme != null)
    {
        theme.value = localTheme;
        docElem.setAttribute('data-theme', theme.value);
    }
};

const toggleTheme = () => {
    if (theme.value == 'light')
    {
        theme.value = 'dark';
    }
    else{
        theme.value = 'light';
    }
    docElem.setAttribute('data-theme', theme.value);
    localStorage.setItem('theme', theme.value);
    console.log(`theme: ${theme.value}`);
};

getSavedTheme();
</script>

<template>
<button @click="toggleTheme">
    <LightTheme v-if="theme === 'light'"/>
    <DarkTheme v-else-if="theme === 'dark'"/>
</button>
</template>

<style scoped>
button {
    --btn-size: 50px;
    display: flex;
    border-radius: 5em;
    align-items: center;
    justify-content: center;
    width: var(--btn-size);
    height: var(--btn-size);
}
svg{
    --icon-size: 80%;
    width: var(--icon-size);
    height: var(--icon-size);
}
</style>