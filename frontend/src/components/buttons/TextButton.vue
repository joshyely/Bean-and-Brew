<script setup>
const props = defineProps({
    color: {
        type: String,
        default: 'var(--color-primary-2)',
    },
    colorText: {
        type: String, 
        default: 'rgb(255, 255, 255)',
    },
    size: {
        type: String,
        default: '1.5em',
    },
});

const style = `
    background-color: ${props.color}; 
    color: ${props.colorText}; 
    font-size: ${props.size}
`;
</script>


<template>
<button :style="style">
    <slot></slot>
</button>
</template>

<style scoped lang="scss">
button {
    border:none;
    padding: .8em 1.5em;
    border-radius: 20px;
    transition: all .25s ease-in;
    &:hover{
        filter: brightness(85%);
        cursor: pointer;
    }
    &:active{
        filter: brightness(50%);
        transform: scale(98%);
    }
    &:disabled{
        opacity: 0.8;
        cursor: not-allowed;
    }
}
</style>