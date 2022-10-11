import api from './axios'

export const postAction = (url, params) => {
    return api({
        url: url,
        method: 'post',
        data: params
    })
}