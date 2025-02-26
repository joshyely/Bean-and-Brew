<script setup>
const props = defineProps({
    heading: String,
    headingSize: {
        type: String,
        default: '3.7em',
    },
});
</script>

<template>
<article>
    <h1 class="heading" :style="`font-size: ${props.headingSize}`">{{ props.heading }}</h1>
    <div class="content">
        <slot></slot>
    </div>
</article>
</template>

<style scoped lang="scss">
article {
    .heading {
        margin-bottom: .2em;
    }
    .content{
        padding: 0 2%;
    }
}
</style>

