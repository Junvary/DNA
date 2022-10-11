import { createApp } from 'vue'
import router from '@/router'
import { store } from '@/store'
import '@/api/permission'
import './style.css'
import App from './App.vue'


const app = createApp(App)
app.use(store).use(router).mount('#app')
