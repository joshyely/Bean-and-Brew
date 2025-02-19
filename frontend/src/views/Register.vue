<script setup>
import { ref, reactive } from 'vue';
import { HttpStatusCode } from 'axios';
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import Alpha from '@/components/form/fields/Alpha.vue';
import Email from '@/components/form/fields/Email.vue';
import Password from '@/components/form/fields/Password.vue';
import NewPassword from '@/components/form/fields/NewPassword.vue';
import Date from '@/components/form/fields/Date.vue';
import { api } from '../utils/axiosAPI';

const formErrMsg = ref('');

// Field models
const models = reactive({
    fName: '',
    lName: '',
    email: '',
    password: '',
    confirmPassword: '',
    dob: '',
});

const submit = () => {
    console.log('submitting..')
    console.log(typeof(models.dob));
    api.post('/auth/register', {
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
};

const submitInvalid = () => {
    console.log('invalid submittion');
    formErrMsg.value = 'Some fields are invalid.';
};
</script>

<template>
<section class="small">
    <Form 
        heading="Register" 
        @submit="submit" 
        @invalid-submit="submitInvalid" 
        id="register" 
        :err-msg="formErrMsg"
    >
        <template #default>
            <Fieldset heading="Personal Info">
                <Alpha
                    id="fName"
                    placeholder="First Name"
                    required
                    v-model="models.fName"
                ></Alpha>
                <Alpha
                    id="lName"
                    placeholder="Last Name"
                    required
                    v-model="models.lName"
                ></Alpha>
                <Date
                    label="Date of Birth (Optional):"
                    v-model="models.dob"
                    min="1-1-1900"
                    max="12-12-2030"
                ></Date>
            </Fieldset>
            <Fieldset heading="Account Security">
                <Email
                    v-model="models.email"
                    required
                ></Email>
                <NewPassword
                    v-model="models.password"
                ></NewPassword>
                <Password
                    placeholder="Confirm Password"
                    v-model="models.confirmPassword"
                ></Password>
            </Fieldset>
        </template>
        <template #lower>
            <p>Already have an account? <RouterLink to="/login">Login here</RouterLink></p>
        </template>
    </Form>
</section>
</template>