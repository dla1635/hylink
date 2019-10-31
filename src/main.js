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

// Axios
import axios from 'axios'
Vue.prototype.$axios = axios

// Vuex
import store from './vuex/store'

// validation
import { Validator } from 'vee-validate'

Vue.use(Validator)

const vue = new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
})

vue.$mount('#app')
