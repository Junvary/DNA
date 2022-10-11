import router from '@/router'
import { useUserStore } from '@/store/user'
import { usePermissionStore } from '@/store/permission'

import { AllowList } from '@/config'

router.beforeEach((to, from, next) => {
    const userStore = useUserStore()
    const permissionStore = usePermissionStore()
    window.$loadingBar.start()
    const token = userStore.GetToken()
    console.log(token, 1)
    if (token) {
        if (AllowList.indexOf(to.path) !== -1) {
            next({ path: '/' })
            window.$loadingBar.finish()
        } else {
            if (!permissionStore.userMenu.length) {
                permissionStore.GetUserMenu().then(res => {
                    if (res) {
                        res.forEach(item => {
                            router.addRoute(item)
                        })
                        next({ ...to, replace: true })
                    } else {
                        userStore.HandleLogout()
                        next({ path: '/', replace: true })
                    }
                })
            } else {
                next()
            }
            window.$loadingBar.finish()
        }
    } else {
        if (AllowList.indexOf(to.path) !== -1) {
            next()
            window.$loadingBar.finish()
        } else {
            next(`/login?redirect=${to.fullPath}`)
            window.$loadingBar.finish()
        }
    }
})

router.afterEach(() => {
    window.$loadingBar.finish()
})