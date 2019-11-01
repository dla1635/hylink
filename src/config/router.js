import Vue from 'vue'
import Router from 'vue-router'

import Welcome from '@/views/Welcome/WelcomePage'
import HomePage from '@/views/Home/HomePage'
import LoginForm from '@/views/Login/LoginForm'
import RegistForm from '@/views/Regist/RegistForm'
import NotFound from '@/components/NotFound'


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
      component: HomePage
    },
    {
      path: '/login',
      name: 'login',
      component: LoginForm
    },
    {
      path: '/regist',
      name: 'regist',
      component: RegistForm
    },
    {
      path: '/notfound',
      name: 'notfound',
      component: NotFound
    },
    {
      path: '*',
      redirect: '/notfound'
    }
  ]
})
