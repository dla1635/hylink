import Vue from 'vue'
import App from '@/App.vue'

// router
import router from './config/router'

// backend
import $backend from './config/backend'
Vue.prototype.$backend = $backend
Vue.config.productionTip = false

// Vuetify
import vuetify from './config/vuetify';
Vue.user(vuetify)

// Axios
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)
Vue.prototype.$axios = axios


// Vuex
import store from './vuex/store'

import VueSession from 'vue-session'
Vue.use(VueSession)

import Swal from 'sweetalert2'
Vue.prototype.$swal = Swal


const vue = new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
})

vue.$mount('#app')
