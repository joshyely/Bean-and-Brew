<!-- Using Vue Options API -->

<script>
export default {
    data() {
        return {
            message: 'Hello World!',
            list: ['Item1', 'Item2', 'Item3'],
            vuejs_link: 'https://vuejs.org/',
            active: true,
            num: 0,
        };
    },
    methods: {
        toggleStatus() {
            if (this.active){
                this.active = false;
            }
            else{
                this.active = true;
            }
        },
        increment() { this.num++ },
        decrement() { this.num-- },
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