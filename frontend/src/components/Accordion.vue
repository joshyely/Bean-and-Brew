<script setup>
import Arrow from '@/components/buttons/GridAccordion.vue';
import { ref } from 'vue';

const show = ref(false);

const toggleShow = () => show.value = !show.value;
</script>

<template>
<div class="accordion">
    <div class="accordion-header">
        <div class="accordion-btn" @click="toggleShow">
            <slot name="button"></slot>
        </div>
    </div>
    <div class="accordion-content" v-show="show">
        <slot></slot>
    </div>
</div>
</template>
<style lang="scss">
.accordion.btn {
    width: fit-content;
}
</style>