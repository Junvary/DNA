import { defineStore } from 'pinia';


export const useUserStore = defineStore('user', {
    state: () => ({
        token: undefined,
        username: undefined,
        nickname: undefined,
        realName: undefined,
        avatar: undefined,
        rememberMe: true,
        language: undefined,
    }),
    actions: {
        GetToken() {
            if (sessionStorage.getItem('gqa-token')) {
                return sessionStorage.getItem('gqa-token')
            } else if (localStorage.getItem('gqa-token')) {
                return localStorage.getItem('gqa-token')
            } else {
                return this.token
            }
        },
        SetToken(token) {
            this.token = token
            localStorage.setItem('dna-token', token)
        }
    }
})