<script setup>
import { computed, provide, ref, VueElement } from 'vue';
import Password from './Password.vue';
import CrossIcon from '@/components/icons/Cross.vue';
import CheckIcon from '@/components/icons/Check.vue';
const vmodel = defineModel();

const regex = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@&£$%^&\(\)-])/;
const minLength = 8;

const regexLower = /[a-z]/;
const regexUpper = /[A-Z]/;
const regexNumber = /[0-9]/;
const regexSymbol = /[@&£$%^&\(\)-]/;


const passwordLower = computed(() => regexLower.test(vmodel.value));
const passwordUpper = computed(() => regexUpper.test(vmodel.value));
const passwordNumber = computed(() => regexNumber.test(vmodel.value));
const passwordSymbol = computed(() => regexSymbol.test(vmodel.value));
const passwordMin = computed(() => vmodel.value.length >= minLength);


</script>

<template>
<Password
    v-model="vmodel"
    :pattern="regex"
    :min="minLength"
    @input=""
    @focusin="showCheckboxes=true"
    @focusout="showCheckboxes=false"
>
    <div class="checkboxes" >
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
            Minimum {{ minLength }} characters
        </div>
    </div>
</Password>

</template>

<style scoped lang="scss">
.checkboxes{
    .checkbox-item{
        display:flex;
        gap:5px;
    }
}

</style>