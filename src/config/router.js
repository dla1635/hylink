import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home/HomePage'

import Welcome from '@/views/Welcome/WelcomePage'

import Login from '@/views/Login/LoginPage'
import Regist from '@/views/Regist/RegistPage'

import NotFound from '@/views/Error/NotFound404'

Vue.use(Router)

const router = new Router({
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
      component: Home,
      meta: {authRequired: true}
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {authRequired: true}
    },
    {
      path: '/regist',
      name: 'regist',
      component: Regist,
    },
    {
      path: '/404',
      name: 'notfound',
      component : NotFound
    },
    {
      path: '*',
      redirect: '/404' 
    },
  ]
})

router.beforeEach(function (to, from, next) {
  // to: 이동할 url에 해당하는 라우팅 객체
  if (to.matched.some(function(routeInfo) {
    return routeInfo.meta.authRequired;
  })) {
    // 이동할 페이지에 인증 정보가 필요하면 경고 창을 띄우고 페이지 전환은 하지 않음
    alert('Login Please!');
    next(false);
  } else {
    next(); // 페이지 전환
  }
});

export default router