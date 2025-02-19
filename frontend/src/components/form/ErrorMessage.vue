

<template>
<div class="err-msg">
    <span class="err-icon"></span>
    <span>
        <slot></slot>
    </span>
</div>
</template>

<style scoped>
.err-msg {
    color:red;
}
</style>