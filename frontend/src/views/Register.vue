<script setup>
import { ref, reactive } from 'vue';
import Alpha from '@/components/form/fields/Alpha.vue';
import Email from '@/components/form/fields/Email.vue';
import NewPassword from '@/components/form/fields/NewPassword.vue';
import DateField from '@/components/form/fields/Date.vue';
import { api } from '../utils/axiosAPI';

// Field models
const formModels = reactive({
    fName: '',
    lName: '',
    email: '',
    password: '',
    confirmPassword: '',
    dob: null,
});
// Objects containing exposed variables belonging to the field components.
const fNameRef = ref();
const lNameRef = ref();
const emailRef = ref();
const newPasswordRef = ref();
const dobRef = ref();

const submit = () => {
    // Validate just in case user doesnt focusin any fields.
    fNameRef.value.validate();
    lNameRef.value.validate();
    emailRef.value.validate();
    newPasswordRef.value.validate();
    dobRef.value.validate();

    console.log(fNameRef.value.isValid);
    if (
        !fNameRef.value.isValid ||
        !lNameRef.value.isValid ||
        !emailRef.value.isValid ||
        !newPasswordRef.value.isValid ||
        !dobRef.value.isValid
    ) {
        return false
    }

    api.post('/auth/register', {
        email: formModels.email,
        password: formModels.password,
        first_name: formModels.fName,
        last_name: formModels.lName,
        dob: formModels.dob,
        recieve_promotions: false,
    })
    .then(response => {
        console.log(response.status);
        console.log(response);
    });
}

</script>

<template>
<div class="wrapper" @click="() => showCheckboxes = false">
<section class="account">
    <h1>Register</h1>
    <br>
    <form @submit.prevent="submit" novalidate id="register">
        <fieldset>
            <h2>Personal Info</h2>
            <Alpha
                id="fName"
                placeholder="First Name"
                required="true"
                v-model="formModels.fName"
                ref="fNameRef"
            ></Alpha>
            <Alpha
                id="lName"
                placeholder="Last Name"
                required="true"
                v-model="formModels.lName"
                ref="lNameRef"
            ></Alpha>
            <DateField
                label="Date of Birth (Optional):"
                v-model="formModels.dob"
                ref="dobRef"
            ></DateField>
        </fieldset>
        <fieldset>
            <h2>Account Security</h2>
            <Email
                v-model="formModels.email"
                ref="emailRef"
                required="true"
            ></Email>

            <NewPassword
                v-model:password="formModels.password"
                v-model:confirm="formModels.confirmPassword"
                ref="newPasswordRef"
            ></NewPassword>
        </fieldset>
        <input type="submit" value="Register">
        <p>Already have an account? <RouterLink to="/login">Login here</RouterLink></p>
    </form>
</section>
</div>

</template>