import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home/HomePage'

import Welcome from '@/views/Welcome/WelcomePage'

import Login from '@/views/Login/LoginPage'
import Regist from '@/views/Regist/RegistPage'

Vue.use(Router)

export default new Router({
  mode : 'history',
  routes: [
    {
      path: '/',
      name: 'welcome',
      component: Welcome
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/regist',
      name: 'regist',
      component: Regist
    }
  ]
})
