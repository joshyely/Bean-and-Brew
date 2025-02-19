<script setup>
import Input from '../Input.vue';

const regex = /^[a-zA-Z]+$/;
const errors = {
    pattern: 'Field can only contain alphabetical characters.',
}

</script>

<template>
<Input
    :pattern="regex"
></Input>
</template>