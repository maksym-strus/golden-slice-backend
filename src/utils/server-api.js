import axios from 'axios'

axios.defaults.withCredentials = true

const server = axios.create({
    baseURL: window.process.env.VUE_APP_BASE_URL
})

server.defaults.xsrfCookieName = 'csrftoken'
server.defaults.xsrfHeaderName = 'X-CSRFToken'

server.interceptors.request.use((config) => {
    const token = localStorage.getItem('accessToken')
    if (token) {
        config.headers['Authorization'] = 'Bearer ' + token
    }

    return config
},null, { synchronous: true })

export default server
