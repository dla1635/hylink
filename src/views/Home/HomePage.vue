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
/* eslint-disable no-console */
import AppBar from './AppBar'
import NavBar from './NavBar'
import CardList from '@/components/CardList'
import Store from '@/vuex/store'
import mapActions from 'vuex'

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
        ...mapActions({
            getCards: 'getCards'
        }),
        // ...mapActions({
        //     postCard: 'postCard'
        // }),
        tmp() {
            const type = this.$route.params.type
            const content = this.$route.params.content
            console.log(type, content)

            const tmpCards = Store.state.layout.card_list;
            console.log(tmpCards)
            if(type === "label") {
                this.card_list = tmpCards.map(function(item){
                    if(item.labels.find() != 'undefind') {
                        return item;
                    }
                });
            } else if(type === 'tag') {
                this.card_list = tmpCards.map(function(item){
                    if(item.tags.find() != 'undefind') {
                        return item;
                    }
                });
            } else {
                this.card_list = tmpCards;
            }
            console.log(this.card_list)
        }
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
