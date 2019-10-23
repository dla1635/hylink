import Vue from 'vue'
import '@/plugins/vuetify'
import App from '@/App.vue'
import router from '@/router'
import $backend from '@/backend'
Vue.prototype.$backend = $backend
Vue.config.productionTip = false

import store from './store'
import axios from 'axios'
Vue.prototype.$axios = axios

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import vuetify from './plugins/vuetify';
Vue.use(Vuetify)
// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
})

vue.$mount('#app')
