<template>
<v-app>

    <!-- 상단 바 -->
    <AppBar ></AppBar>

    <!--  Side bar    -->
    <NavBar  />

    <!-- 웰컴 바 -->
    

    <v-content>
        <router-view />
    </v-content>

</v-app>
</template>

<script>
import AppBar from '@/components/AppBar'
import NavBar from '@/components/NavBar'

export default {
    name: 'App',
    data: () => ({
        navBarDrawer: false,
        AppBarDrawer: false,
        isLogin: false,
    }),
    components: {
        AppBar,
        NavBar
    },
    methods: {

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
