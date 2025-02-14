<script setup>
import { ref, computed, watch } from 'vue';
import Field from './Field.vue';

const props = defineProps({
    id: String,
    label: String,
    required: Boolean = false,
    maxYear: Number,
    minYear: Number,
})



const MaxYear = props.maxYear!=null ? props.maxYear : new Date().getFullYear();
const MinYear = props.minYear!=null ? props.minYear : 1900;

const day = ref('');
const month = ref('');
const year = ref('');

const isValid = ref(false);
const isValidated = ref(false);
const errorMessage = ref('');

const vmodelDate = defineModel();

const monthNames = [
    "January",
    "February", 
    "March", 
    "April", 
    "May", 
    "June", 
    "July", 
    "August", 
    "September", 
    "October", 
    "November", 
    "December"
];
const years = computed(() => {
  const list = [];
  for (let i = MaxYear; i >= MinYear; i--) {
    list.push(i);
  }
  return list;
})
const days = ref(31);
watch([year, () => month.value], ([year, month])  => {
    days.value = new Date(
        year=='' ? 2000 : year,
        month=='' ? 1 : month+1,
        0
    )
    .getDate();
});

const validate = () => {
    let noneSelected = (
        day.value == '' &&
        month.value == '' &&
        year.value == ''
    )
    if (!props.required && noneSelected) {
        isValid.value = true;
        errorMessage.value = '';
        vmodelDate.value = null;
        return
    }

    isValidated.value = true;
    if (
        day.value == '' ||
        month.value == '' ||
        year.value == ''
    ) {
        isValid.value = false;
        errorMessage.value = 'Not all fields have been selected.';
        vmodelDate.value = null;
    }
    else {
        isValid.value = true;
        errorMessage.value = '';
        vmodelDate.value = new Date(year.value, month.value, day.value);
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
    class="date margin-top"
>
    <label v-if="!!props.label">{{ props.label }}:</label>
    <div class="field-flex" @focusout="validate">
        <select :key="days" name="day" id="day" v-model="day" :class="[day==='' ? 'default': '', !isValid && isValidated ? 'invalid' : '']">
            <option class="placeholder" value="">Day</option>
            <hr>
            <option v-for="dayOpt in days" :value="dayOpt" >{{ dayOpt }}</option>
        </select>
        <select name="month" id="month" v-model="month" :class="[month==='' ? 'default': '', !isValid && isValidated ? 'invalid' : '']">
            <option class="placeholder" value="">Month</option>
            <hr>
            <option v-for="(monthName, index) in monthNames" :key="index" :value="index">{{ monthName }}</option>
        </select>
        <select name="year" id="year" v-model.number="year" :class="[year==='' ? 'default': '', !isValid && isValidated ? 'invalid' : '']">
            <option class="placeholder" value="">Year</option>
            <hr>
            <option v-for="n in years" :value="n">{{ n }}</option>
        </select>
    </div>
</Field>

</template>