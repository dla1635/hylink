<template>
<v-app-bar app clipped-left color="white">
    <v-app-bar-nav-icon @click="changeNavBarState()"></v-app-bar-nav-icon>
    <v-img src="@/assets/logo.png" max-width="50"></v-img><span class="title ml-3 mr-5">Hylink</span>
    <v-text-field text hide-details prepend-inner-icon="search" v-model="search_word" @keyup.enter="search"></v-text-field>
    <v-flex align-center d-flex flex-row-reverse mr-5>
        <v-btn icon>
            <img src="https://www.w3schools.com/css/paris.jpg" style="width:50px; height:50px; border-radius: 50%;" />
        </v-btn>
        <span style="font-size:20px; line-height:24px; margin-right:5px;">종완띠</span>
    </v-flex>
</v-app-bar>
</template>

<script>
/* eslint-disable */

export default {    
    name: 'AppBar',
    data() {
        return {
            drawer: true,
            search_word: ""
        }
    },
    methods: {
        changeNavBarState() {
            this.$store.commit('changeNavBarState');
        },
        async search() {
            console.log('search1')
            const payload = {
                type: 'word',
                word: this.search_word,
            }
            await this.$store.dispatch('search', payload)

            await this.$router.push({name:'home', params: { type:'search'}}).catch(err => {})
        }
    }
}
</script>
