<script setup>
import { ref, computed, watch, reactive } from 'vue';
import Select from '../Select.vue';
import ErrorMessage from '../ErrorMessage.vue';

const props = defineProps({
    label: String,
    required: {
        type: Boolean,
        default: false,
    },
    maxYear: {
        type: Number,
        default: new Date().getFullYear(),
    },
    minYear: {
        type: Number,
        default: 1900,
    },
});




const fields = reactive({
    day: '',
    month: '',
    year: '',
});
const invalid = reactive({
    day: false,
    month: false,
    year: false,
});

const errMsg = ref('');

const vmodelDate = defineModel();

const months = [
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
  for (let i = props.maxYear; i >= props.minYear; i--) {
    list.push(i);
  }
  return list;
})
const days = ref(31);

watch(monyear, (month, year) => {
    fields.day.value = new Date(
        year=='' ? 2000 : year,
        month=='' ? 1 : month+1,
        0
    )
    .getDate();
});

const checkFieldsEmpty = () => {
    for(let field in fields){
        console.log(field);
    } 
}

const validate = () => {
    let noneSelected = (
        fields.day.value == '' &&
        fields.month.value == '' &&
        fields.year.value == ''
    )
    if (!props.required && noneSelected) {
        errMsg.value = '';
        vmodelDate.value = null;
        return true
    }

    if (
        fields.day.value == '' ||
        fields.month.value == '' ||
        fields.year.value == ''
    ) {
        errMsg.value = 'Not all fields have been selected.';
        vmodelDate.value = null;
    }
    else {
        errMsg.value = '';
        vmodelDate.value = new Date(year.value, month.value, day.value);
    }
};
</script>

<template>
    <div class="date" @focusout="validate">
        <label v-if="!!props.label">{{ props.label }}</label>
        <div class="group-items">
            <Select
                placeholder="Day"
                :options="days"
                :invalid="!!errMsg"
                v-model="fields.day.value"
            ></Select>
            <Select
                placeholder="Month"
                :options="months"
                :invalid="!!errMsg"
                v-model="fields.month.value"
            ></Select>
            <Select
                placeholder="Year"
                :options="years"
                :invalid="!!errMsg"
                v-model="fields.year.value"
            ></Select>
        </div>
        <ErrorMessage v-show="!!errMsg">{{ errMsg }}</ErrorMessage>
    </div> 
</template>
    
<style scoped lang="scss">
.date{
    height: 10vh;
    .group-items{
        display:flex;
        gap: 1.2%;
        margin: .8vh 0 0.4vh;
    }
}
</style>