import { defineStore } from 'pinia'
import { postAction } from '@/api/manage'


export const usePermissionStore = defineStore('permission', {
    state: () => ({
        userMenu: [],
        searchMenu: [],
        topMenu: []
    }),
    actions: {
        async GetUserMenu() {
            // const res = await postAction('user/get-user-menu')
            // if (res.code === 1) {
            //     const data = res.data.records
            //     // 拿到鉴权路由表（用户自己的所有菜单），整理成路由
            //     const userMenu = HandleRouter(data)
            //     // 加入404界面
            //     userMenu.push({
            //         path: '/:catchAll(.*)*',
            //         name: 'notFound',
            //         // component: () => import('pages/Error404.vue')
            //     })
            //     // 设置所有菜单
            //     this.InitUserMenu(userMenu)
            //     // 去掉隐藏菜单
            //     const searchMenu = data.filter(value => value.hidden === "no")
            //     // 设置搜索菜单
            //     this.InitSearchMenu(searchMenu)
            //     // 深度拷贝，避免影响其他数据
            //     const searchMenuNew = JSON.parse(JSON.stringify(searchMenu))
            //     const topMenu = ArrayToTree(searchMenuNew, "name", "parent_code")
            //     this.InitTopMenu(topMenu)

            //     // 返回鉴权路由表
            //     return userMenu
            // } else {
            //     return
            // }
        },
    }
})