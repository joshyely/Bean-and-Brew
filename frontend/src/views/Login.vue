<script setup>
import { ref, reactive } from 'vue'
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import Email from '@/components/form/fields/Email.vue';
import Password from '@/components/form/fields/Password.vue';
import { apiFormUrlEncoded } from '../utils/axiosAPI';
import { HttpStatusCode } from 'axios';
import { login } from '@/utils/auth';


const models = reactive({
    email: '',
    password: ''
});
const loginErrs = reactive({
    formErrMsg: '',
    credentialsInvalid: false,
});

const submit = () => {
    console.log(models.email);
    console.log(models.password);
    apiFormUrlEncoded.post('/auth/login',
        {
            username: models.email,
            password: models.password,
        })
        .then(response => {
            console.log('login success!');
            login(response.data.access_token);
        })
        .catch(error => {
            console.log('error!')
            console.log(error)
            switch (error.status) {
                case HttpStatusCode.Unauthorized:
                    loginErrs.formErrMsg = 'Email or Password was incorrect.'
                    loginErrs.credentialsInvalid = true
                    break;
                default:
                    loginErrs.formErrMsg = error.message;
            }
        });
}
</script>


<template>
    <section class="form">
        <Form heading="Login" :err-msg="loginErrs.formErrMsg" @submit="submit">
            <template #default>
                <Fieldset @input="loginErrs.credentialsInvalid = false">
                    <Email v-model="models.email" :err="loginErrs.credentialsInvalid"></Email>
                    <Password v-model="models.password" :err="loginErrs.credentialsInvalid"></Password>
                </Fieldset>
            </template>
            <template #lower>
                <p>Don't have an account? <RouterLink to="/register">Register here</RouterLink>
                </p>
            </template>
        </Form>
    </section>
</template>

<style scoped lang="scss"></style>