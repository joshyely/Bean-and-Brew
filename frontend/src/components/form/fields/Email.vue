<script setup>
import { computed, provide, ReactiveEffect, ref } from 'vue';
import Input from '../Input.vue';

const regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

const errors = {
    pattern: 'Invalid Email.',
    max: 'Email can not be over 50 characters long.'
}

</script>

<template>
<Input
    type="email"
    placeholder="Email"
    :pattern="regex"
    :max="50"
    :errors="errors"
></Input>
</template>