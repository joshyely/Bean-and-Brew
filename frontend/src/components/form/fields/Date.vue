<script setup>
import { watch, reactive, computed } from 'vue';
import Input from '../Input.vue';

const props = defineProps({
    min: {
        type: [String, Number],
        default: null,
    },
    max: {
        type: [String, Number],
        default: Date.now(),
    },
})

const errors = {
    min: 'Date cannot be older than minimum date',
    max: 'Date cannot be greater than maximum date'
}

</script>

<template>
<Input
    type="date"
    field-class="date-field"
    :class="['date-input']"
    :errors="errors"
    :min=props.min
    :max=props.max
>
    <template #helper>
        <div class="date-helper">
            <p v-if="!!props.min">Min Date: {{ props.min }}</p>
            <p v-if="!!props.max">Max Date: {{ props.max }}</p>
        </div>
    </template>
</Input>
</template>

<style>
.field.date-field .input-container .input-inner{
    right: 2.5em;
}
</style>

<style scoped lang="scss">
.date-helper {
    display: flex;
    justify-content: space-between;
    padding: 0 1.5%;
}
</style>