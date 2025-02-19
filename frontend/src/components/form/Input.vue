<script setup>
import { inject, onMounted, ref, computed } from 'vue';
import ErrorMessage from './ErrorMessage.vue';
import UniqueID from '@/utils/uniqueID.js';
import { validPattern, notEmpty, sameAs, differentTo } from '@/utils/validation';

const inputID = ref(
  UniqueID()
);
var inputElem;
onMounted(()=>{
  inputElem = document.getElementById(inputID.value);
});

const props = defineProps({
  type: {
    type: String,
    default: 'text',
  },
  required: {
    type: Boolean,
    default: false,
  },
  min: Number,
  max: Number,
  pattern: {
    type: RegExp,
    default: null,
  },
  same: {
    type: String,
    default: null,
  },
  different: {
    type: [String, Array],
    default: null,
  },
  errors: {
    type: Object,
    default(newProps){
      return {}
    },
  },
  doValidate: {
    type: Boolean,
    default: true,
  },
  validateOnInput: {
    type: Boolean, 
    default: false,
  }
});

const errMsg = ref(null);
const vmodel = defineModel();

const errors = {
  blank: 'Field cannot be blank.',
  min: `Cannot be less than ${props.min}.`,
  max: `Cannot be more than ${props.max}.`,
  pattern: 'Field doesn\'t match the required pattern.',
  notSame: 'Fields dont match.',
  notDifferent: 'Fields cannot be the same.',
  ...props.errors
};


const getSize = () => {
  switch(props.type)
  {
    case 'date':
      return new Date(vmodel.value);
    case 'number':
      return Number(vmodel.value);
    default:
      return vmodel.value.length;
  }
};

const min = computed(() => {
  switch(props.type){
    case 'date':
      return Number(props.min) || Date.parse(props.min) || null;
    default:
      return Number(props.min) || null;
  }
});

const max = computed(() => {
  switch(props.type){
    case 'date':
      return Number(props.max) || Date.parse(props.max) || null;
    default:
      return Number(props.max) || null;
  }
});

const validated = ref(false);

const validate = () => {
  console.log(`${min.value}\n${max.value}`);
  if (!props.doValidate) {
    return true
  }

  let size = getSize();
  
  if (!notEmpty(vmodel.value)){
    errMsg.value = props.required ? errors.blank : '';
  }
  else if (!validPattern(vmodel.value, props.pattern)) {
    errMsg.value = errors.pattern;
  }
  else if (min.value!=null && size < min.value) {
    errMsg.value = errors.min;
  } 
  else if (max.value!=null && size > max.value) {
    errMsg.value = errors.max;
  }
  else if (differentTo(vmodel.value, props.same))
  {
    errMsg.value = errors.notSame;
  }
  else if (sameAs(vmodel.value, props.different))
  {
    errMsg.value = errors.notDifferent;
  }
  else {
    errMsg.value = '';
  }

  validated.value = true;
  return !!errMsg.value;
};

const showHelper = ref(false);

const validations = inject('validations', []);
validations.push(validate);
</script>

<template>
<div class="field">
  <div
    v-if="$slots.helper" 
    v-show="showHelper" 
    :class="['helper', !!errMsg ? 'invalid' : validated&!!String(vmodel) && 'valid']"
  >
      <slot name="helper"></slot>
  </div>
  <div
    :class="['input-container',
      !!errMsg ? 'invalid' : validated&!!String(vmodel) && 'valid',
      $slots.helper ? 'has-helper' : ''
    ]"
    @input="validate()"
    @focusin="showHelper=true"
    @focusout="showHelper=false"
  >
    
    <input 
      :type="props.type" 
      placeholder="text" 
      v-bind="$attrs" v-model="vmodel" 
      :class="['field-input', !!String(vmodel) || 'empty']"
      :id="inputID"
      :min="min"
      :max="max"
    >
    <div class="input-components">
        <slot></slot>
    </div>
  </div>
  
  <ErrorMessage v-show="!!errMsg">{{ errMsg }}</ErrorMessage>
</div>
</template>

<style scoped lang="scss">

.field{
  margin: 1.2vh 0;
  position:relative;
  .helper{
    position: absolute;
    z-index: 10;
    bottom: 100%;
    width:100%;
    background-color: var(--color-background);
    border: var(--border-hover);
    border-bottom:none;
    padding: 1vh 5%;
  }
  .input-container {
    border: var(--border);
    border-radius: 5px;
    height: 38px;
    display:flex;
    align-items: center;
    transition: border 0.2s ease-in-out;
    position:relative;
    &:focus-within{
      border: var(--border-hover);
      &.has-helper{
        border-top-right-radius: 0%;
        border-top-left-radius: 0%;
      }
    }
  
    input {
      background: none;
      border: none;
      padding: 0 1.2em;
      margin: 0;
      width: 100%;
      height: 100%;
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
    }
    .input-components{
      position: absolute;
      width:fit-content;
      right:.6em;
      left:auto;
    }
  }
}
</style>
