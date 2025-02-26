<template>
<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed">
    <path d="M480-344 240-584l56-56 184 184 184-184 56 56-240 240Z" />
</svg>
</template>

<style scoped lang="scss">
svg {
    --size: 80px;
    width: var(--size);
    height: var(--size);
    display:flex;
    justify-content: center;
    align-items: center;
    border-radius: 100%;
    background-color: var(--color-primary-2);
    transition: all .25s ease-in;
    &:hover{
        cursor: pointer;
        background-color: var(--color-primary-3);
        transform: scale(1.01);
    }
}
</style>

