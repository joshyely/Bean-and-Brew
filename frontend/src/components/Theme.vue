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
<div id="theme-btn" @click="toggleTheme">
    <LightTheme id="light-icon" v-if="theme === 'light'"/>
    <DarkTheme id="dark-icon" v-else-if="theme === 'dark'"/>
</div>
</template>

<style scoped>


#theme-btn {
    --btn-size: 25px;
    display: flex;
    border-radius: 50%;
    align-items: center;
    justify-content: center;
    width: var(--btn-size);
    height: var(--btn-size);
    border-style: none;
}
#theme-btn:hover svg{
    fill: var(--color-theme-icon-hover);
    cursor:pointer;
    transition: fill .25s ease;
}

#theme-btn svg {
    fill: var(--color-theme-icon);
}

@media (max-width: 1024px) {
    #theme-btn{
        --btn-size:32px;
        margin: 10px;
    }
}
</style>