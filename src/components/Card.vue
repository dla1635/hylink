<template>
    <v-card class="card">   
        <v-list-group expand="false">
            <template v-slot:activator>
                <!-- <v-layout>
                    <v-flex class="card_detail">
                        <span style="font-size:20px;">{{card.title}}</span><br/>
                        <span class="tag" v-for="tag in card.tagList" :key="tag">
                            #{{tag}}
                        </span>
                    </v-flex>
                    <img class="card_img" :src="card.thumbnail">
                </v-layout> -->
            </template>
            
            <!-- <v-list-item-content style="padding:0 30px;">
                <v-layout>
                    <v-flex class="card_detail">
                    <span style="font-size:20px;">{{card.title}}</span><br/>
                    <span class="tag" v-for="tag in card.tagList" :key="tag">
                        #{{tag}}
                    </span>
                </v-flex>
                <img class="card_img" :src="card.thumbnail">
                </v-layout>
            </v-list-item-content> -->
        </v-list-group>
    </v-card>
</template>

<script>
export default {
	name: 'Card',
	props: {
        card: {type:Object},
        index: {type:Number},
    },
    methods: {
    }
}
</script>

<style scoped>

.card {
  margin: 5px 10px;
}


.card_detail {
    padding:10px;
}
.card_img {
    width: 100px;
    height: 100px;
}
.tag {
    margin-right:5px;
}

#cardContainer {
}
</style>
