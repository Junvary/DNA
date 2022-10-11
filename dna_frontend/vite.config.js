import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import ViteComponents from 'unplugin-vue-components/vite'
import { NaiveUiResolver } from 'unplugin-vue-components/resolvers'

// https://vitejs.dev/config/
export default defineConfig(envConfig => {
    const viteEnv = loadEnv(envConfig.mode, process.cwd())
    return {
        plugins: [
            vue(),
            ViteComponents({
                resolvers: [NaiveUiResolver()]
            })
        ],
        resolve: {
            alias: [
                {
                    find: '@/',
                    replacement: path.resolve(process.cwd(), 'src') + '/',
                }
            ]
        },
        server: {
            open: true,
            port: viteEnv.VITE_CLI_PORT,
            proxy: {
                // 把key的路径代理到target位置
                // detail: https://cli.vuejs.org/config/#devserver-proxy
                [viteEnv.VITE_BASE_API]: { // 需要代理的路径   例如 '/api'
                    target: `${viteEnv.VITE_BASE_PATH}`, // 代理到 目标路径
                    changeOrigin: true,
                    rewrite: path => path.replace(new RegExp('^' + viteEnv.VITE_BASE_API), ''),
                }
            },
        }
    }
})
