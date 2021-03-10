const auth = {
    state: {
        isAuth: false
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
