<template>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="24px" fill="#e8eaed">
    <path d="M291-253.85 253.85-291l189-189-189-189L291-706.15l189 189 189-189L706.15-669l-189 189 189 189L669-253.85l-189-189-189 189Z"/>
    <circle class="sb-icon-hover" cx="50%" cy="-50%" r="50%"></circle>
</svg>
</template>

<style scoped>
svg{
    height: 40px;
    width: 40px;
}
circle{
    opacity: .15;
    fill: transparent;
    transition: fill .15s ease-in-out;
}
svg {
    width: 85px;
}
svg:hover {
    cursor:pointer;
}
svg:hover circle{
    fill:initial;
}
svg:active{
    transform:scale(95%);
}
</style>