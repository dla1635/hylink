<template>
  <v-app>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
/*eslint no-console: "error"*/
import AppBar from '@/components/AppBar'
import NavBar from '@/components/NavBar'

export default {
  name: 'App',
  data() {
    return {
    };
  },
  components: {

  },
};
</script>
