<script setup>
import Accordion from './Accordion.vue';
import GridAccordion from './buttons/GridAccordion.vue';


const props = defineProps({
    columns: {
        type: String,
        default: '1fr 1fr',
    },
    rows: {
        type: String,
        default: 'auto',
    },
});

</script>

<template>
    <div class="grid-container">
        <div class="grid">
            <slot></slot>
        </div>
        <div class="accordion" v-if="$slots.accordion">
            <div class="button">
                <GridAccordion></GridAccordion>
            </div>
            <div class="overlay"></div>
            <div class="grid">
                <slot name="accordion"></slot>
            </div>
        </div>

    </div>
</template>

<style scoped lang="scss">
.grid-container{
    --gap-y: 30px;
    .grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        width: 100%;
        gap: var(--gap-y) 20px;
        @media(max-width: 1024px){
            grid-template-columns: 1fr !important;
        }
    }
    .accordion {
        margin-top: var(--gap-y);
        height: 6.5vh;
        position: relative;
        overflow: hidden;
        .overlay {
            position: absolute;
            z-index: 10;
            bottom: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(transparent, var(--color-background));
        }
        .button{
            position: absolute;
            z-index: 11;
            bottom: 0;
            right: 1%;
        }
    }
}


</style>