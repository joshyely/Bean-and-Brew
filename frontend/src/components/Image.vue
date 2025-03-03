<script setup>
const props =  defineProps({
    src: {
        type: String,
        default: '../assets/blankImage.png',
    },
    alt: {
        type: String,
        default: 'Blank Image',
    },
});

const loadImage = () => props.src;
</script>

<template>
<img :src="props.src" :alt="props.alt">
</template>

<style scoped>
img {
    width:100%;
    object-fit: cover;
}
</style>