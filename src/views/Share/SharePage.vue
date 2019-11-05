<template>
<v-container>
    <!-- 상단 바 -->
    <AppBar></AppBar>

    <v-container>
        <v-card flat outlined class="pl-5" v-if="title != ''">
            <h1> {{title}} </h1>
        </v-card>
        <v-list three-line>
            <template v-for="(card, index) in card_list">

                <v-divider v-if="card.divider" :key="index"></v-divider>

                <v-list-item v-else :key="card.title">

                    <v-list-item-content justify="center" >
                        <v-container to="login">
                            <v-row>
                                <v-col :cols="8">
                                    <v-row>
                                        <v-list-item-title>
                                            <a v-bind:href="card.url" style="color: black; text-decoration: none;">
                                            <h2>{{card.title}}</h2>
                                            </a>
                                        </v-list-item-title>
                                    </v-row>
                                    <v-row>
                                        <v-list-item-content>
                                            {{card.summary}}
                                        </v-list-item-content>
                                    </v-row>
                                    <v-row align-self="end">
                                        <v-chip-group multiple column>
                                            <v-chip v-for="t in card.tag" :key="t.name">
                                                {{ t.name }}
                                            </v-chip>
                                        </v-chip-group>
                                    </v-row>

                                </v-col>
                                <v-col :cols="4" >
                                    <a v-bind:href="card.url" style="color: black; text-decoration: none;">
                                    <v-img :src="card.thumbnail" height="150" contain></v-img>
                                    </a>
                                </v-col>

                            </v-row>

                        </v-container>

                    </v-list-item-content>
                </v-list-item>
            </template>

        </v-list>
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
            card_list:[],
        }
    },
    mounted() {
        //axios를 이용해 데이터 가져오기
        this.getCards();
    },
    methods : {
        async getCards(){
            const shareCode = this.$route.params.shareCode;
            this.card_list = await this.$axios.get('http://127.0.0.1:8000/api/share/'+shareCode+"/")
            .then(
                function(response){
                    var cardList = [];
                    console.log(response);
                    for(var i = 0; i< response.data.sharelink.length; i+=1){
                        cardList.push(response.data.sharelink[i].link);
                        cardList.push({ divider: true, inset: true });
                    }
                    return cardList;
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
