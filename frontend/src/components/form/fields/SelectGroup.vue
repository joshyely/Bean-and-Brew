<script setup>
import { ref } from 'vue';
import ErrorMessage from '../ErrorMessage.vue';

const props = defineProps({
    label: String,
    required: {
        type: Boolean,
        default: false,
    },
});

const errMsg = ref('');

const validate = () => {

};

</script>

<template>
<div class="select-group" @focusout="validate">
    <label v-if="!!props.label">{{ props.label }}</label>
    <div class="group-items">
        <slot></slot>
    </div>
    <ErrorMessage v-show="!!errMsg">{{ errMsg }}</ErrorMessage>
</div> 
</template>

<style scoped lang="scss">
.select-group{
    height: 10vh;
    .group-items{
        display:flex;
        gap: 1.2%;
        margin: .8vh 0 0.4vh;
    }
}
</style>