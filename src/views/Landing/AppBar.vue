<template>
<<<<<<< HEAD:src/views/Welcome/AppBar.vue
    <v-app-bar app clipped-left hide-on-scroll color="ffffff00">
        <!-- <router-link to="home">
            <v-img src="@/assets/logo.png" max-width="50"></v-img>
        </router-link> -->
        <router-link to="home" id=welcome-logo>
            Hylink
            <!-- <v-img src="@/assets/txtLogo.png" max-width="100"></v-img> -->
        </router-link>
=======
<v-app-bar app clipped-left color="white">
>>>>>>> 09dc263d52de5f3b065dd59d28994b55967a6bd3:src/views/Landing/AppBar.vue

        <v-spacer></v-spacer>

        <v-btn text depressed to="login" color="#009CEE">
            Login
        </v-btn>
        <v-btn v-if="islogin" text depressed to="logout" color="#009CEE">
            Logout
        </v-btn>
        <v-btn text depressed to="regist" color="#009CEE">
            Register
        </v-btn>

    </v-app-bar>
</template>

<script>
export default {
    name: 'AppBar',
    data() {
        return {
            islogin: false
        }
    },
    methods: {

    }
}
</script>

<style scoped>
#welcome-logo {
    font-family: 'Ubuntu', sans-serif;
    font-weight: 500;
    font-size: 1.5em;
    text-decoration: none !important;
    color: #01E6E6;
}
</style>>
