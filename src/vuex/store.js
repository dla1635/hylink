import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/dist/logger';
//import { Mutations } from './mutations.js'
//import { Actions } from './actions.js'

import auth from './auth';
import signup from './signup';
import { layout } from './layout.js'

const debug = process.env.NODE_ENV !== 'production';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  //mutations: Object.assign({}, Mutations),
  //actions: Object.assign({}, Actions),
  modules: {
    layout,
    auth,
    signup
  },
  strict: debug,
  plugins: debug ? [createLogger()] : [],
})
