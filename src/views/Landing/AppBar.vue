<template>
<v-app-bar app clipped-left color="white">

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
