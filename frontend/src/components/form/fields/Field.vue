<script setup>
const props = defineProps({
    id: String,
    class: String,
    errMsg: String,
    valid: Boolean,
    validated: Boolean = true,
});

</script>

<template>
<div :id="id" :class="['field', props.class, !props.valid && props.validated ? 'invalid' : '']">
    <slot />

    <span v-if="!!props.errMsg && !props.valid && props.validated" class="invalid-msg">{{ props.errMsg }}</span>
</div>
</template>