<script setup>
import { ref } from 'vue';
const props = defineProps({
    valid: {
        type: Boolean,
        default: true,
    }
});

const showHelper = ref(false);
</script>

<template>
<div
    :class="['input-container',
        !props.valid ? 'invalid' : '',
        $slots.helper ? 'has-helper' : ''
    ]"
    @focusin="showHelper=true"
    @focusout="showHelper=false"
>
    <slot></slot>
    <div class="input-components">
        <slot name="input-components"></slot>
    </div>
</div>
<div v-if="$slots.helper" v-show="showHelper" class="helper">
    <slot name="helper"></slot>
</div>
</template>

<style scoped lang="scss">
.input-container {
    border: var(--border);
    border-radius: 5px;
    height: 38px;
    display:flex;
    align-items: center;
    transition: border 0.2s ease-in-out;
    position:relative;
    &:focus-within{
        border: var(--border-hover);
        &.has-helper{
        border-bottom-right-radius: 0%;
        border-bottom-left-radius: 0%;
        }
    }

    input {
        background: none;
        border: none;
        padding: 0 1.2em;
        margin: 0;
        width: 100%;
        height: 100%;
        font-size: 1.1em;
        font-family: Arial, Helvetica, sans-serif;
        &:focus{
        border:none;
        outline: none;
        }
        &::-ms-reveal,
        &::-ms-clear
        {
        display: none;
        }
    }
    .input-components{
        position: absolute;
        width:fit-content;
        right:.6em;
        left:auto;
    }
    &.invalid {
        border-color: rgb(200, 0, 0) !important;
        box-shadow: 0px 0px 4px rgb(250, 150, 150);
    }
}
</style>