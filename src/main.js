import Vue from 'vue'
import '@/plugins/vuetify'
import App from '@/App.vue'
import router from '@/router'
import $backend from '@/backend'

Vue.prototype.$backend = $backend
Vue.config.productionTip = false

// Vuetify
import vuetify from './plugins/vuetify';

// Axios
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

// Vuex
import store from './store/store'

const vue = new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
})

vue.$mount('#app')
