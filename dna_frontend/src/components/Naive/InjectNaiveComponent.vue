<template></template>

<script setup>
import { useDialog, useLoadingBar, useMessage, useNotification } from 'naive-ui';

window.$loadingBar = useLoadingBar()
window.$dialog = useDialog()
window.$message = useMessage()
window.$notification = useNotification()
</script>