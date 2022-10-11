<template>
    <n-loading-bar-provider>
        <n-dialog-provider>
            <n-notification-provider>
                <n-message-provider>
                    <router-view />
                    <!-- 注入 loadingBar dialog message notification -->
                    <InjectNaiveComponent />
                </n-message-provider>
            </n-notification-provider>
        </n-dialog-provider>
    </n-loading-bar-provider>
</template>

<script setup>
import InjectNaiveComponent from '@/components/Naive/InjectNaiveComponent.vue'
</script>