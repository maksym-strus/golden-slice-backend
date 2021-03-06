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
    children: [
      { path: 'login', name: 'Login', component: () => import('../views/Login') },
      { path: 'register', name: 'Register', component: () => import('../views/Register') }
    ]
  },
  {
    path: '/',
    name: 'Main',
    component: Main,
    children: [
      { path: 'about', name: 'About', component: () => import( '../views/About') },
      { path: 'home', name: 'Home', component: () => import('../views/Home') }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
