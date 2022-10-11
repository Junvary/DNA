import axios from 'axios'
import { useUserStore } from '@/store/user'

const api = axios.create({
    baseURL: import.meta.env.VITE_BASE_API,
    timeout: 45000
})

api.interceptors.request.use(request => {
    const userStore = useUserStore()
    const token = userStore.GetToken()
    request.headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Dna-Token': token
    }
    return request
}, error => {
    return error
})

api.interceptors.response.use(response => {
    const responseData = response.data
    const { code } = responseData
    if (code === 1) {
        return response.data
    } else {
        return response.data
    }
}, error => {
    return error
})

export default api