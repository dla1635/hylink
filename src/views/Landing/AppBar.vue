<template>
<v-app-bar app clipped-left color="white">

    <router-link to="home/label/total">
        <v-img src="@/assets/logo.png" max-width="50"></v-img>

    </router-link>
    <router-link to="home/label/total">
        <v-img src="@/assets/txtLogo.png" max-width="100"></v-img>

    </router-link>

    <v-spacer></v-spacer>

    <v-btn text depressed to="login" color="transparent">
        Login
    </v-btn>
    <v-btn text depressed to="register" color="transparent">
        Register
    </v-btn>
</v-app-bar>
</template>

<script>
export default {
    name: 'AppBar',
    data() {
        return {}
    },
    methods: {}
}
</script>
