<template>
    <n-form ref="formRef" :label-width="80" :model="formValue" :rules="rules">
        <n-form-item label="用户名" path="username">
            <n-input v-model:value="formValue.username" placeholder="请输入用户名" />
        </n-form-item>
        <n-form-item label="密码" path="password">
            <n-input v-model:value="formValue.password" placeholder="请输入密码" />
        </n-form-item>
        <n-form-item>
            <n-button @click="login">
                登录
            </n-button>
        </n-form-item>
    </n-form>
</template>

<script setup>
import { ref } from "vue";
import { postAction } from "@/api/manage";
import { useUserStore } from '@/store'

const userStore = useUserStore()
const formRef = ref(null)
const formValue = ref({
    username: '',
    password: '',
})
const rules = {
    username: {
        required: true,
        message: "请输入用户名",
        trigger: "blur"
    },
    password: {
        required: true,
        message: "请输入密码",
        trigger: "blur"
    },
}
const login = (e) => {
    e.preventDefault();
    formRef.value?.validate((errors) => {
        if (!errors) {
            postAction('system/login/', {
                username: formValue.value.username,
                password: formValue.value.password
            }).then(res => {
                if (res.code === 1) {
                    const token = res.data.data
                    userStore.SetToken(token)
                } else {
                    window.$message.error(res.message);
                }
            })
        } else {
            window.$message.error("Invalid");
        }
    });
}
</script>