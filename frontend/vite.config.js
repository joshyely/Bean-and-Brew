import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

const API_URL = process.env.VITE_API_URL || 'http://localhost:5000/';
console.log('API_URL: ', API_URL);

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      'vue': 'vue/dist/vue.esm-bundler',
    },
  },
  // dev: {
  //   proxy: {
  //     '/api': {
  //       target: API_URL,
  //       changeOrigin: true,
  //     },
  //   },
  // },
  // server: {
  //   proxy: {
  //     '/api': {
  //       target: API_URL,
  //       changeOrigin: true,
  //     },
  //   },
  // },
  // build: {
  //   outDir: 'dist',
  //   sourcemap: false,
  //   proxy: {
  //     '/api': {
  //       target: API_URL,
  //       changeOrigin: true,
  //     },
  //   },
  // },
})
