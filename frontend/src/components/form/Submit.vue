<script setup></script>

<template>
<input type="submit" value="Submit">
</template>

<style scoped>
input[type=submit]{
    height: 45px;
    width: 100px;
    border-radius: var(--border-radius);
    border: 1px solid var(--color-primary-2);
    background-color: var(--color-primary-2);
    font-size: 1.25em;
    color: rgb(255, 255, 255);
    transition: all 0.2s ease-in-out;
}
input[type=submit]:hover{
    cursor: pointer;
    background-color: var(--color-primary-3);
    border-color: var(--color-primary-3);
}
</style>