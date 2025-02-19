<script setup>
import { ref } from 'vue'
import Input from '../Input.vue'
import ShowIcon from '../../icons/Show.vue';
import HideIcon from '../../icons/Hide.vue';


const passwordShow = ref(false);
const passwordToggle = () => passwordShow.value = !passwordShow.value;
</script>

<template>
<Input
    :type="!passwordShow ? 'password' : 'text' " 
    placeholder="Password"
    required
>
    <template #default>
        <span class="password-toggle-btn" @click="passwordToggle">
            <ShowIcon v-if="passwordShow"/>
            <HideIcon v-else/>
        </span>
    </template>
    <template #helper v-if="$slots.default">
        <slot></slot>
    </template>
</Input>
</template>

<style lang="scss" scoped>

</style>