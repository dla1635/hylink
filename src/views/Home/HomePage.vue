<template>
<v-app id="container">
    <!-- 상단 바 -->
    <AppBar></AppBar>

    <!--  Side bar    -->
    <NavBar />

    <v-container fluid>
        <v-text-field
            id="url_input"
            v-model="url_input"
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
import {mapActions} from 'vuex'

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
            url_input:""
        };
    },
    watch: {
        changeParams: function() {
            this.tmp()
        }
    },
    computed: {
        changeParams: function(){
            return this.$route.params;
        }
    },
    methods: {
        ...mapActions({getCards: 'getCards'}),
        tmp() {
            this.card_list=[]
            const type = this.$route.params.type
            const content = this.$route.params.content
            const tmpCards = Store.state.layout.card_list;

            if(type === "label") {
                this.card_list = tmpCards.filter(function(item){
                    if(item.label.find(function(item){return item.name === content})) {
                        return item;
                    }
                });
            } else if(type === 'tag') {
                this.card_list = tmpCards.filter(function(item){
                    if(item.tag.find(function(item){return item.name === content})) {
                        return item;
                    }
                });
            } else {
                this.card_list = tmpCards;
            }
        },
        postCard() {
            this.$store.dispatch("postCard",{url:this.url_input})
        }
    },
    async mounted() {
        await this.getCards()
        this.tmp()
    }
};
</script>

<style scoped>
#container {
    background-color: white;
}

</style>
