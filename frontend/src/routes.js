import { createMemoryHistory, createRouter, createWebHistory } from 'vue-router'

import Home from './views/Home.vue'
import About from './views/About.vue'
import Contact from './views/Contact.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'
import Profile from './views/Profile.vue'


const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/about', component: About, name: 'About' },
    { path: '/contact', component: Contact, name: 'Contact' },
    { path: '/login', component: Login, name: 'Login' },
    { path: '/register', component: Register, name: 'Register' },
    { path: '/profile', component: Profile, name: 'Profile' },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;