import Vue from 'vue'
import Router from 'vue-router'

import Landing from '@/views/Landing/LandingPage'
import HomePage from '@/views/Home/HomePage'
import LoginPage from '@/views/Login/LoginPage'
import SharePage from '@/views/Share/SharePage'
import RegistPage from '@/views/Regist/RegistPage'
import NotFound404 from '@/views/Error/NotFound404'


Vue.use(Router)

const router = new Router({
  mode : 'history',
  routes: [
    {
      path: '/',
      name: 'landing',
      component: Landing
    },
    {
      path: '/home/:type/:content',
      name: 'home',
      component: HomePage
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
      path: '/share/:shareCode',
      name: 'share',
      component: SharePage
    },
    {
      path: '/notfound',
      name: 'notfound',
      component: NotFound404
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