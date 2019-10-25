import Vue from 'vue'
import '@/plugins/vuetify'
import App from '@/App.vue'
import router from '@/router'
import $backend from '@/backend'
Vue.prototype.$backend = $backend
Vue.config.productionTip = false

import store from './store/store'
import axios from 'axios'
Vue.prototype.$axios = axios

import VueSession from 'vue-session'
Vue.use(VueSession)

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import vuetify from './plugins/vuetify';
Vue.use(Vuetify)
// Vue.use(VueRouter)

import VueSweetalert2 from 'vue-sweetalert2';
// 스타일 커스터마이징 
import 'sweetalert2/dist/sweetalert2.min.css'
Vue.use(VueSweetalert2)
Vue.prototype.$swal = VueSweetalert2

const vue = new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
})

vue.$mount('#app')
