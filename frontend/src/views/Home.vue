<script setup>
import { reactive, ref } from 'vue';
import BaseField from '../components/form/fields/Field.vue'
import Email from '../components/form/fields/Email.vue'

const form = reactive({
    email: '',
})


const emailRef = ref();

</script>

<template>
    <h1>Home</h1>
    <p>{{ form.email }}</p>
    <p>{{ emailRef }}</p>

    <form @submit.prevent="onSubmit">
        <Email
            v-model="form.email"
            ref="emailRef"
        />
        <input type="submit" value="Submit">
    </form>
    
</template>