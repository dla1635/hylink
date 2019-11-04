<template>
<v-app-bar app clipped-left color="amber">

    <router-link to="home">
        <v-img src="@/assets/logo.png" max-width="50"></v-img>

    </router-link>
    <router-link to="home">
        <v-img src="@/assets/txtLogo.png" max-width="100"></v-img>

    </router-link>

</v-app-bar>
</template>

<script>
export default {
    name: 'AppBar',
    data() {
        return {}
    },
    methods: {

    }
}
</script>
