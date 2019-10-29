import Vue from 'vue'
import Router from 'vue-router'

import Welcome from '@/views/Welcome/WelcomePage'
import HomePage from '@/views/Home/HomePage'
import LoginPage from '@/views/Login/LoginPage'
import RegistPage from '@/views/Regist/RegistPage'
import AboutUs from '@/components/template/AboutUs'
import NotFound from '@/components/template/NotFound'

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
      component: LoginPage
    },
    {
      path: '/regist',
      name: 'regist',
      component: RegistPage
    },
    {
      path: '/aboutus',
      name: 'aboutus',
      component: AboutUs
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
