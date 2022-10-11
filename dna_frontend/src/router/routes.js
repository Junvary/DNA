// 公共路由，无须鉴权
export const PublicRoutes = [
    {
        path: '/login',
        name: 'login',
        component: () => import('@/layouts/LoginLayout/index.vue'),
        children: []
    },
    {
        path: '/new-tab',
        component: () => import('@/layouts/NewTabLayout/index.vue'),
        children: []
    }
]

export const PrivateRoutes = [
    {
        path: '/',
        redirect: { path: '/dashboard' },
        component: () => import('@/layouts/MainLayout/index.vue'),
        children: []
    }
]

export default [...PublicRoutes, ...PrivateRoutes]