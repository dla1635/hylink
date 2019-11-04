<template>
<v-container>
    <!-- 상단 바 -->
    <AppBar></AppBar>

    <v-container>
        <v-card flat outlined class="pl-5" v-if="title != ''">
            <h1> {{title}} </h1>
        </v-card>
        <v-list three-line>
            <template v-for="(card, index) in cards">

                <v-divider v-if="card.divider" :key="index"></v-divider>

                <v-list-item v-else :key="card.title">

                    <v-list-item-content justify="center" >
                        <v-container to="login">
                            <v-row>
                                <v-col :cols="8">
                                    <v-row>
                                        <v-list-item-title>
                                            <h2>{{card.title}}</h2>
                                        </v-list-item-title>
                                    </v-row>
                                    <v-row>
                                        <v-list-item-content>
                                            {{card.content}}
                                        </v-list-item-content>
                                    </v-row>
                                    <v-row align-self="end">
                                        <v-chip-group multiple column>
                                            <v-chip v-for="tag in card.tags" :key="tag">
                                                {{ tag }}
                                            </v-chip>
                                        </v-chip-group>
                                    </v-row>

                                </v-col>
                                <v-col :cols="4" >
                                    <v-img :src="card.thumbnail" height="200"></v-img>
                                </v-col>

                            </v-row>

                        </v-container>

                    </v-list-item-content>
                </v-list-item>
            </template>

        </v-list>

        <CardList :cardList="card_list" />
    </v-container>
</v-container>
</template>

<script>
/* eslint-disable no-console */
import AppBar from './AppBar'

export default {
    name: 'SharePage',
    components: {
        AppBar,
    },
    data() {
        return {
            title : "",
            cards: [{
                    thumbnail: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    content: "Ali Connors I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                    tags: ['algo', 'bigdata']
                },
                {
                    divider: true,
                    inset: true
                }, {
                    thumbnail: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    content: "Ali Connors &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                    tags: ['algo', 'bigdata']
                },
                {
                    divider: true,
                    inset: true
                }, {
                    thumbnail: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    content: "Ali Connors &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                    tags: ['algo', 'bigdata']
                }, {
                    divider: true,
                    inset: true
                }, {
                    thumbnail: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    content: "Ali Connors &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                    tags: ['algo', 'bigdata']
                },

            ]
        }
    },
    mounted() {
        //axios를 이용해 데이터 가져오기
        this.getCards();
    },
    methods : {
        getCards : function(){
            this.$axios.get('http://13.125.61.163:8000/api/share/')
            .then(
                function(response){
                    console.log(response);
                }
            )
            .catch(
                function(error){
                    console.log(error);
                }
            );
        }
    }

};
</script>

<style>
img {
    max-height: 100%;
}
</style>
