<template>
  <v-app>
<<<<<<< HEAD
    <!-- 라우터뷰는 NavBar에 존재    -->
    <NavBar/>
=======
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        text
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>
    </v-app-bar>

    <v-content>
      <Login></Login>
      <Regist></Regist>
    </v-content>
>>>>>>> e9f0bbed7d8c1729f04443e5a82ea7f40e44d5c5
  </v-app>
</template>

<script>
<<<<<<< HEAD
import NavBar from '@/components/NavBar'

=======
import Login from './components/Login'
import Regist from './components/Regist'
>>>>>>> e9f0bbed7d8c1729f04443e5a82ea7f40e44d5c5
export default {
  data() {
    return {
    };
  },
  components: {
<<<<<<< HEAD
    NavBar
=======
    Login,
    Regist
>>>>>>> e9f0bbed7d8c1729f04443e5a82ea7f40e44d5c5
  },
};
</script>s
