<template>
<v-app id="container">
        <!-- 상단 바 -->
    <AppBar></AppBar>

    <!--  Side bar    -->
    <NavBar v-if="navBarDrawer" />
    404 ERROR!
</v-app>
</template>

<script>
import AppBar from './AppBar'
import NavBar from './NavBar'

export default {
    name: "404",
    components: {
        AppBar,
        NavBar,
    },
    data() {
        return {
            navBarDrawer: false,
            AppBarDrawer: false,
        }
    },
    computed: {
        drawerState() {
            return this.$store.getters.getNavBarState;
        },

    },
    watch: {
        drawerState(val) {
            this.navBarDrawer = val;
        },
    }
};
</script>

<style scoped>
#container {
    background-color: white;
}
</style>
