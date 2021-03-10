import Vue from 'vue'
import VueRouter from 'vue-router'
import Auth from "../views/Auth";
import Main from "../views/Main";

Vue.use(VueRouter)

const routes = [
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
  {
    path: '/',
    name: 'Main',
    component: Main,
    redirect: '/home',
    children: [
      { path: 'about', name: 'About', component: () => import( '../views/About') },
      { path: 'home', name: 'Home', component: () => import('../views/Home') },
      { path: 'result/:id', name: 'Result', component: () => import('../views/Result') },
      { path: 'result', name: 'ResultList', component: () => import('../views/ResultList')}
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
