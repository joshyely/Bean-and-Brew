<script setup>
import { provide } from 'vue';
import Submit from './Submit.vue';
import ErrorMessage from './ErrorMessage.vue';
import Fieldset from './Fieldset.vue';

const props = defineProps({
    heading: String,
    validate: {
        type: Boolean,
        default: true,
    },
    errMsg: {
        type: String,
        default: '',
    },
});


const validations = [];
provide('validations', validations);

const emit = defineEmits(['invalid-submit', 'submit']);

const doSubmit = () => {
    if(props.validate){
        let valid = true;
        validations.forEach(validate => {
            if (!validate()) {
                valid = false;
            }
        });
        if(valid) {
            emit('submit', true);
        }
        else {
            emit('invalid-submit', true);
        }
    } 
};


</script>

<template>
<div>
<h1>{{ props.heading }}</h1>
<br>
<div class="form-container">
    <form @submit.prevent="doSubmit" novalidate>
        <div class="form-default">
            <slot></slot>
        </div>
        <Fieldset>
            <div class="form-lower">
                <ErrorMessage class="form-error">{{ props.errMsg }}</ErrorMessage>
                <Submit></Submit>
                <div class="lower-slot">
                    <slot name="lower"></slot>
                </div>
            </div>
        </Fieldset>
        
    </form>
</div>

</div>
</template>

<style lang="scss">
.form-container{
    h2{
        border-bottom: var(--border);
        padding: 0 5%;
    }
}


.form-default{
    margin-bottom: .5vh;
}
.form-error{
    margin-bottom: 1vh;
}
.lower-slot{
    margin-top: 4vh;
}

</style>