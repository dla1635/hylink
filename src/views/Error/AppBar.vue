<template>
<v-app-bar app clipped-left color="amber">
    <router-link to="home">
        <v-img src="@/assets/logo.png" max-width="50"></v-img><span class="title ml-3 mr-5">Hylink</span>
        <v-text-field text hide-details prepend-inner-icon="search"></v-text-field>
    </router-link>
    <v-flex align-center>
        <v-btn icon>
            <img src="https://www.w3schools.com/css/paris.jpg" style="width:50px; height:50px; border-radius: 50%;" />
        </v-btn>
        <span style="font-size:20px; line-height:24px;">종완띠</span>
    </v-flex>
</v-app-bar>
</template>

<script>
export default {
    name: 'AppBar',
    data() {
        return {
            drawer: false
        }
    },
    methods: {
        changeNavBarState() {
            this.$store.commit('changeNavBarState');
        }
    }
}
</script>
