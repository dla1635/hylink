import Vue from 'vue'
import '@/plugins/vuetify'
import App from '@/App.vue'
import router from '@/router'
import $backend from '@/backend'
Vue.prototype.$backend = $backend
Vue.config.productionTip = false

import vuetify from './plugins/vuetify';
// Vue.use(VueRouter)

import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

const vue = new Vue({
  router,
  vuetify,
  render: h => h(App)
})

vue.$mount('#app')
