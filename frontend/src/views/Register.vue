<script setup>
import { ref, reactive } from 'vue';
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import Alpha from '@/components/form/fields/Alpha.vue';
import Email from '@/components/form/fields/Email.vue';
import Password from '@/components/form/fields/Password.vue';
import NewPassword from '@/components/form/fields/NewPassword.vue';
import Date from '@/components/form/fields/Date.vue';
import { apiJSON } from '../utils/axiosAPI';
import axios, { HttpStatusCode } from 'axios';



// Field models
const models = reactive({
    fName: '',
    lName: '',
    email: '',
    password: '',
    confirmPassword: '',
    dob: null,
});


const registrationErrs = reactive({
    formErrMsg: '',
    email: { msg: '', invalid: false },
    confirmPassword: { msg: '', invalid: false },
});

const checkPasswordsMatch = () => {
    if (!models.password || !models.confirmPassword) {
        return true;
    }

    if (models.password != models.confirmPassword) {
        registrationErrs.confirmPassword.msg = 'Passwords do not match.';
        return false;
    }
    registrationErrs.confirmPassword.msg = '';
    return true;
};

const submit = async () => {
    apiJSON.post('/auth/register', {
        email: models.email,
        password: models.password,
        first_name: models.fName,
        last_name: models.lName,
        dob: models.dob,
        recieve_promotions: false,
    })
    .catch(error => {
        console.log(error);
        formErrMsg.value = error.message;
    })
    .then(response => {
        console.log('success!');
    });
}

const submitInvalid = () => {
    console.log('invalid submittion');
    formErrMsg.value = 'Some fields are invalid.';
};
</script>

<template>
    <section class="form">
        <Form heading="Register" @submit="submit" @invalid-submit="submitInvalid" id="register"
            :err-msg="registrationErrs.formErrMsg">
            <template #default>
                <Fieldset heading="Personal Info">
                    <Alpha id="fName" placeholder="First Name" required v-model="models.fName"></Alpha>
                    <Alpha id="lName" placeholder="Last Name" required v-model="models.lName"></Alpha>
                    <Date label="Date of Birth (Optional):" v-model="models.dob" min="1-1-1900" max="12-12-2030"></Date>
                </Fieldset>
                <Fieldset heading="Account Security">
                    <Email v-model="models.email" :err="registrationErrs.email" required></Email>
                    <NewPassword v-model="models.password" @focusout="checkPasswordsMatch"></NewPassword>
                    <Password placeholder="Confirm Password" v-model="models.confirmPassword"
                        :err="registrationErrs.confirmPassword" @focusout="checkPasswordsMatch"></Password>
                </Fieldset>
            </template>
            <template #lower>
                <p>
                    Already have an account? <RouterLink to="/login">Login here</RouterLink>
                </p>
            </template>
        </Form>
    </section>
</template>