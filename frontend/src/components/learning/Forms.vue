<script setup>
import { ref } from 'vue';

const tasks = ref([])
const newTask = ref('')

const addTask = () => {
    if (newTask.value.trim()) {
        tasks.value.push(newTask.value);
        newTask.value = '';
        console.log(tasks.value);
    }
};
const deleteTask = index => {
    tasks.value.splice(index, 1);
    console.log(tasks.value);
};
</script>

<template>
<div id="tasks-container">
    <h1>Tasks</h1>
    <div id="tasks">
        <ul>
            <li v-for="(task, index) in tasks" :key="task">
                <span>{{ task }}</span>
                <button @click="deleteTask(index)">x</button>
            </li>
        </ul>
    </div>
    <form @submit.prevent="addTask">
        <label for="newTask">Add Task: </label>
        <input type="text" id="newTask" name="newTask" v-model="newTask">
    </form>
</div>
</template>

<style>
form{
    width: 50%;
    padding: 3%;
}


#tasks ul{
    list-style: none;
}
</style>