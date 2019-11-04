<template>
<v-app id="container">
    <!-- 상단 바 -->
    <AppBar></AppBar>

    <!--  Side bar    -->
    <NavBar v-if="navBarDrawer" />

    <v-container fluid>
        <v-text-field
            id="url_input"
          solo
          text
          hide-details
          label="URL"
          prepend-inner-icon="link"
          style="width:900px; padding:0 10%;"
            @keyup.enter="postCard"
      ></v-text-field>
        <CardList :cardList="card_list" />
    </v-container>
</v-app>
</template>

<script>
import AppBar from './AppBar'
import NavBar from './NavBar'
import CardList from '@/components/CardList'
import Store from '@/vuex/store'

export default {
    name: "HomePage",
    components: {
        AppBar,
        NavBar,
        CardList
    },
    data() {
        return {
            card_list:[]
        };
    },
    computed: {
    },
    methods: {
        // ...mapActions({
        //     getCards: 'getCards'
        // }),
        // ...mapActions({
        //     postCard: 'postCard'
        // }),
    },
    mounted() {
        this.getCards()
        this.card_list = Store.state.layout.card_list
    },
    beforeUpdate() {
        this.card_list = Store.state.layout.card_list
    }
};
</script>

<style scoped>
#container {
    background-color: white;
}

</style>
