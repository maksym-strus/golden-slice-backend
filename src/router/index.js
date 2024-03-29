import Vue from 'vue'
import VueRouter from 'vue-router'
import Auth from '../views/Auth';
import Main from '../views/Main';
import store from '../store';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main,
    redirect: '/home',
    meta: {
      requiresAuth: true
    },
    children: [
      { path: 'about', name: 'About', component: () => import( '../views/About') },
      { path: 'home', name: 'Home', component: () => import('../views/Home') },
      { path: 'result/:id', props: true, name: 'Result', component: () => import('../views/Result') },
      { path: 'result', name: 'ResultList', component: () => import('../views/ResultList')}
    ]
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth,
    redirect: '/auth/login',
    children: [
      { path: 'login', name: 'Login', component: () => import('../views/Login') },
      { path: 'register', name: 'Register', component: () => import('../views/Register') }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: window.process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuth) {
      next()
    } else {
      next('auth')
    }
  }
  next()
})

export default router
