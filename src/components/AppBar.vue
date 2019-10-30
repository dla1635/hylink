<template>
<v-app-bar app clipped-left color="white">
    <v-app-bar-nav-icon @click="changeNavBarState()"></v-app-bar-nav-icon>
    <v-img src="@/assets/logo.png" max-width="50"></v-img><span class="title ml-3 mr-5">Hylink</span>
    <v-text-field text hide-details prepend-inner-icon="search"></v-text-field>
    <v-flex align-center d-flex flex-row-reverse mr-5>
        <v-btn icon>
            <img src="https://www.w3schools.com/css/paris.jpg" style="width:50px; height:50px; border-radius: 50%;" />
        </v-btn>
        <span style="font-size:20px; line-height:24px; margin-right:5px;">종완띠</span>
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
