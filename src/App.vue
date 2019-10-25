<template>
<v-app>

    <!-- 상단 바 -->
    <AppBar></AppBar>

    <!--  Side bar    -->
    <NavBar/>

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
        //
    }),
    components: {
    AppBar,
    NavBar
  },
};
</script>