<script setup>
import { computed, provide, ReactiveEffect, ref } from 'vue';
import Field, {  } from './Field.vue';

const props = defineProps({
    required: Boolean = false,
});

const vmodel = defineModel();

const isValid = ref(false);
const isValidated = ref(false);
const errorMessage = ref('');

const regexEmail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;



const validate = () => {
    let isEmpty = vmodel.value.trim() == '';
    if (!props.required && isEmpty){
        isValid.value = true;
        errorMessage.value = '';
        return
    }

    isValidated.value = true;
    if(isEmpty)
    {
        isValid.value = false;
        errorMessage.value = 'Field cannot be blank.';
    }
    else if(!regexEmail.test(vmodel.value))
    {
        isValid.value = false;
        errorMessage.value = 'Invalid email.';
    }
    else
    {
        isValid.value = true;
        errorMessage.value = '';
    }
    
};

defineExpose({
    isValid,
    validate,
});
</script>

<template>
<Field
  class="email-field"
  :valid="isValid"
  :err-msg="errorMessage"
  :validated="isValidated"
>
    <input
        type="email"
        placeholder="Email"
        v-model="vmodel"
        @focusout="validate"
    >

</Field>

</template>