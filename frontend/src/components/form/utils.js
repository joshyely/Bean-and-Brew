import { provide, inject } from "vue";

export const errors = {
    blank: 'Field cannot be blank.',
    alpha: 'Field can only contain alphabetical characters.',
    passwordCriteria: 'Password does not meet the criteria.',
    passwordMismatch: 'Passwords do not match.',
    emailInvalid: 'Invalid email.',
    selectionMissing: 'Not all fields have been selected.',
}


class Data {
    validations = [];
}

export const data = new Data() 



