<script setup>
import { computed, ref } from 'vue';
import Field from './Field.vue';
import CheckIcon from '../../icons/Check.vue';
import CrossIcon from '../../icons/Cross.vue';
import ShowIcon from '../../icons/Show.vue';
import HideIcon from '../../icons/Hide.vue';

const props = defineProps({
    id: String,
    placeholder: String,
})

const vmodelPassword = defineModel('password');
const vmodelConfirm = defineModel('confirm')

const isValid = computed(() => isValidPassword && isValidConfirm);
const isValidPassword = ref(false);
const isValidConfirm = ref(false);

const isValidatedPassword = ref(false);
const errorMessagePassword = ref('');
const isValidatedConfirm = ref(false);
const errorMessageConfirm = ref('');

const regexLower = /[a-z]/;
const regexUpper = /[A-Z]/;
const regexNumber = /[0-9]/;
const regexSymbol = /[@&£$%^&\(\)-]/;

const passwordLower = computed(() => regexLower.test(vmodelPassword.value));
const passwordUpper = computed(() => regexUpper.test(vmodelPassword.value));
const passwordNumber = computed(() => regexNumber.test(vmodelPassword.value));
const passwordSymbol = computed(() => regexSymbol.test(vmodelPassword.value));
const passwordMin = computed(() => vmodelPassword.value.length >= 8);


const validateNewPassword = () => {
    isValidatedPassword.value = true;
    validateConfirmPassword();

    if (vmodelPassword.value.trim() == '') {
        isValidPassword.value = false;
        errorMessagePassword.value = 'Field cannot be blank.';
    }
    else if (
        !passwordLower.value || 
        !passwordUpper.value || 
        !passwordNumber.value || 
        !passwordSymbol.value || 
        !passwordMin.value
    ) {
        isValidPassword.value = false;
        errorMessagePassword.value = 'Password does not meet the criteria.';
    }
    else{
        isValidPassword.value = true;
        errorMessagePassword.value = '';
    }
};
const validateConfirmPassword = () => {
    isValidatedConfirm.value = true;
    if (vmodelConfirm.value.trim() == '') {
        isValidConfirm.value = false;
        errorMessageConfirm.value = 'Field cannot be blank.';
    }
    else if (vmodelConfirm.value != vmodelPassword.value) {
        isValidConfirm.value = false;
        errorMessageConfirm.value = 'Passwords do not match.';
    }
    else{
        isValidConfirm.value = true;
        errorMessageConfirm.value = '';
    }
};

const validate = () => {
    validateNewPassword();
    validateConfirmPassword();
};

const passwordShow = ref(false);
const confirmPasswordShow = ref(false);
const passwordToggle = () => passwordShow.value = !passwordShow.value;
const confirmPasswordToggle = () => confirmPasswordShow.value = !confirmPasswordShow.value;

defineExpose({
    isValid,
    validate,
});
</script>


<template>
<Field
    class="new-password-field"
    :valid="isValidPassword"
    :err-msg="errorMessagePassword"
    :validated="isValidatedPassword"
>
    <input 
        :type="[!passwordShow ? 'password' : 'text' ]" 
        placeholder="Password"
        v-model="vmodelPassword"
        @focusout="validateNewPassword"
    />
    <span class="password-toggle-btn" @click="passwordToggle(passwordShow)">
        <ShowIcon v-if="passwordShow"/>
        <HideIcon v-else/>
    </span>
    <div class="checkboxes">
        <div class="checkbox-item">
            <span>
                <CheckIcon v-if="passwordLower"/>
                <CrossIcon v-else/>
            </span>
            Lowercase
        </div>
        <div class="checkbox-item">
            <span>
                <CheckIcon v-if="passwordUpper"/>
                <CrossIcon v-else/>
            </span>
            Uppercase
        </div>
        <div class="checkbox-item">
            <span>
                <CheckIcon v-if="passwordNumber"/>
                <CrossIcon v-else/>
            </span>
            Number
        </div>
        <div class="checkbox-item">
            <span>
                <CheckIcon v-if="passwordSymbol"/>
                <CrossIcon v-else/>
            </span>
            Symbol
        </div>
        <div class="checkbox-item">
            <span>
                <CheckIcon v-if="passwordMin"/>
                <CrossIcon v-else/>
            </span>
            Minimum 8 characters
        </div>
    </div>
</Field>
<Field
    class="password-field"
    :valid="isValidConfirm"
    :err-msg="errorMessageConfirm"
    :validated="isValidatedConfirm"
>
    <input 
        :type="[!confirmPasswordShow ? 'password' : 'text' ]"
        placeholder="Confirm Password" 
        v-model="vmodelConfirm"
        @focusout="validateConfirmPassword"
    />
    <span class="password-toggle-btn" @click="confirmPasswordToggle">
        <ShowIcon v-if="confirmPasswordShow"/>
        <HideIcon v-else/>
    </span>
</Field>

</template>