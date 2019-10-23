<template>
<v-app>
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
export default {
    name: 'App',
    data: () => ({
        //
    }),
};
</script>
