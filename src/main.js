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

import Swal from 'sweetalert2'
Vue.prototype.$swal = Swal


const vue = new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
})

vue.$mount('#app')
