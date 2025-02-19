<script setup>
import { inject, popScopeId, ref } from 'vue';
const props = defineProps({
    placeholder: {
        type: String,
        default: 'Select',
    },
    options: {
        type: [Object , Set, Array, Number],
    },
    required: {
        type: Boolean,
        default: false,
    },
}); 

const vmodel = defineModel({default:''});

const errMsg = ref('');

const validate = () => {
    if(!props.required){
        errMsg.value = '';
    } else if (vmodel.value == ''){
        errMsg.value = 'Field required.'
    }
    else {
        errMsg.value = ''
    }
    return errMsg.value == ''
}


const validations = inject('validations');
validations.push(validate);
</script>

<template>
<div
    :class="['select-wrapper', !!errMsg ? 'invalid' : !!String(vmodel) && 'valid']"
    @focusout="validate"
>
    <select :class="[!!String(vmodel) || 'default']" v-model="vmodel">
        <option class="placeholder" value="">{{ props.placeholder }}</option>
        <hr>
        <option
        v-for="name, value in props.options" 
        :value="value"
        >
            {{ name }}
        </option>
    </select>
</div>
</template>

<style scoped lang="scss">

.select-wrapper {
    border: var(--border);
    border-radius: var(--border-radius-2);
    height: 38px;
    display:inline-flex;
    align-items: center;
    select {
        border:none;
        background: none;
        width: 100%;
        height:100%;
        padding: 0 1.2em;
        font-size: 1.1em;
        font-family: Arial, Helvetica, sans-serif;
        &:focus{
            border:none;
            outline: none;
        }
        &::-ms-reveal,
        &::-ms-clear
        {
            display: none;
        }
        &.default {
            color: var(--color-text-3);
        }
        hr {
            color: var(--color-border)
        }
        option {
            display: block;
            align-content: center;
            height: 4vh;
            margin:0;
            padding: 0 1em;
            color: var(--color-text);
            &.placeholder{
                color: var(--color-text-3);
            }
        }
        &:focus-within { 
            .box-container {
                border: var(--border-hover);
            }
        }
    }       
}

</style>