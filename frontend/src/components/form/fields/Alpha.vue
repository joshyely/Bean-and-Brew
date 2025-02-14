<script setup>
import { ref } from 'vue';
import Field from './Field.vue';

const props = defineProps({
    id: String,
    placeholder: String,
    required: Boolean = false,
})

const vmodel = defineModel();

const isValid = ref(false);
const isValidated = ref(false);
const errorMessage = ref('');

const regexAlpha = /^[a-zA-Z]+$/;



const validate = () => {
    let isEmpty = vmodel.value.trim() == '';
    if (!props.required && isEmpty){
        isValid.value = true;
        errorMessage.value = '';
        return
    }

    isValidated.value = true;
    if (isEmpty) {
        isValid.value = false;
        errorMessage.value = 'Field cannot be blank.';
    }
    else if (!regexAlpha.test(vmodel.value)) {
        isValid.value = false;
        errorMessage.value = 'Field can only contain alphabetical characters.';
    }
    else{
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
    :valid="isValid"
    :err-msg="errorMessage"
    :validated="isValidated"
>
    <input
        type="text"
        :placeholder="props.placeholder"
        v-model="vmodel"
        @focusout="validate"
    >
</Field>

</template>