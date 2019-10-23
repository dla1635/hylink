import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'

import Login from '@/views/LoginPage'
import Regist from '@/views/RegistPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
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
