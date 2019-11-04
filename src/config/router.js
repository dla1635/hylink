import Vue from 'vue'
import Router from 'vue-router'

import Welcome from '@/views/Welcome/WelcomePage'
import HomePage from '@/views/Home/HomePage'
import LoginPage from '@/views/Login/LoginPage'
import RegistPage from '@/views/Regist/RegistPage'
import NotFound from '@/components/NotFound'


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

router.beforeEach(function (to, from, next) {
  // to: 이동할 url에 해당하는 라우팅 객체
  if (to.matched.some(function(routeInfo) {
    return routeInfo.meta.authRequired;
  })) {
    // 인증 정보가 없으면 이전 페이지로 돌아감
    next(false);
  } else {
    next(); // 페이지 전환
  }
});

export default router