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
// import mapActions from 'vuex'

export default {
    name: "HomePage",
    components: {
        AppBar,
        NavBar,
        CardList
    },
    data() {
        return {
            card_list:[],
            tmp_list: []
        };
    },
    watch: {
        changeParams: function() {
            this.tmp()
            return this.$route.params
        }
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
        this.tmp()
    }
};
</script>

<style scoped>
#container {
    background-color: white;
}

</style>
