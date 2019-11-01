<template>
<v-app>

<<<<<<< HEAD
=======
    <!-- 상단 바 -->
    <AppBar ></AppBar>

    <!--  Side bar    -->
    <NavBar  />

    <!-- 웰컴 바 -->
    

>>>>>>> a704d32957696c8cca6b8826c39f9eb4dc142659
    <v-content>
        <router-view />
    </v-content>

</v-app>
</template>

<script>

export default {
    name: 'App',
    data: () => ({
<<<<<<< HEAD
        
=======
        navBarDrawer: false,
        AppBarDrawer: false,
        isLogin: false,
>>>>>>> a704d32957696c8cca6b8826c39f9eb4dc142659
    }),
    components: {
        
    },
    methods: {

    },
    
};
</script>
