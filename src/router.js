import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/views/HomePage'
import LoginPage from '@/views/LoginPage'
// import Messages from '@/components/Messages'

Vue.use(Router)

export default new Router({
  mode : 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    }
    // {
    //   path: '/messages',
    //   name: 'messages',
    //   component: Messages
    // }
  ]
})
