<script setup>
const props = defineProps({
    heading: String,
});
</script>

<template>
<fieldset>
    <h2 v-if="!!heading" class="fieldset-heading">{{ props.heading }}</h2>
    <div class="fieldset-content">
        <slot></slot>
    </div>
</fieldset>
</template>

<style scoped lang="scss">
fieldset{
    .fieldset-content {
        display:flex;
        flex-direction: column;
        align-items: center;
        & > *{
            width: 95%;
        }
    }
    border: none;
    .fieldset-heading {
        padding: .8vh 5%;
        margin-bottom: 1.5vh;
        border-bottom: var(--border);
    }
}
</style>