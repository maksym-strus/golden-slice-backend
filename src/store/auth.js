const auth = {
    state: {
        isAuth: !!localStorage.getItem('accessToken')
    },
    getters: {
        isAuth: (state) => state.isAuth
    },
    mutations: {
        setAuth (state, value) {
            state.isAuth = value
        }
    },
    actions: {
        setAuth (store, value) {
            store.commit('setAuth', value)
        }
    }
}

export default auth
