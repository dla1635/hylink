<template>
<v-app>
    <!-- 라우터뷰는 NavBar에 존재    -->
    <NavBar/>

    <v-app-bar app>
        <v-toolbar-title class="headline text-uppercase">
            <router-link to="/"> <span>TEST</span> </router-link>
        </v-toolbar-title>

    </v-app-bar>

    <v-content>
        <router-view />
    </v-content>
    
</v-app>
</template>

<script>

import NavBar from '@/components/NavBar'

export default {
    name: 'App',
    data: () => ({
        //
    }),
    components: {
    NavBar
  },
};
</script>s
