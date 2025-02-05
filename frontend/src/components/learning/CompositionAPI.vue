<!-- Using Vue Composition API -->

<script>
import { ref } from 'vue';
export default {
    setup() {
        const message = 'Hello World';
        const active = ref(true);
        const list = ['Item1', 'Item2', 'Item3'];
        const vuejs_link = 'https://vuejs.org/';
        const num = ref(0);

        const toggleStatus = () => {
            if (active.value) {
                active.value = false;
            }
            else {
                active.value = true;
            }
        };
        const increment = () => num.value++;
        const decrement = () => num.value--;
        
        return {
            message,
            active,
            list,
            vuejs_link,
            num,
            toggleStatus,
            increment,
            decrement, 
        }
    },

};
</script>

<template>
    <h5>Message: <span>{{ message }}</span></h5>
    <ul>
        <li v-for="item in list" :key="item">{{ item }}</li>
    </ul>
    <a :href="vuejs_link">Vue.js Website</a>
    <p v-if="active">Active User</p>
    <p v-else>Inactive User</p>
    <button v-on:click="toggleStatus">Change User Status</button>
    <br>
    <p>Number: {{ num }}</p>
    <div style="display:flex; flex-direction: row-reverse;">
        <button @click="increment">Increment</button>
        <button @click="decrement">Decrement</button>
    </div>
</template>