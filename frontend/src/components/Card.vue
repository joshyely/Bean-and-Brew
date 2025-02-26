<script setup>
import placeholders from '@/utils/placeholders';
import Image from './Image.vue';

const props = defineProps({
    heading: {
        type: String,
        default: placeholders.heading,
    },
    text: {
        type: String,
        default: placeholders.paragraph,
    },
    imageSrc: String,
    imageAlt: String,
});

</script>

<template>
    <div class="card">
        <Image :src="props.imageSrc" :alt="props.imageAlt"></Image>
        <div class="content">
            <h2 class="heading">{{ props.heading }}</h2>
            <p>{{ props.text }}</p>
        </div>
    </div>
</template>

<style scoped lang="scss">
.card {
    box-shadow: var(--box-shadow);
    border-radius: var(--border-radius-2);
    transition: all .25s ease-in;
    img {
        object-fit: cover;
    }
    .content{
        padding: 0 24px 20px;
    }
    .heading {
        margin-bottom: 1vh;
    }
    &:hover {
        box-shadow: var(--box-shadow-hover);
    }
}
</style>