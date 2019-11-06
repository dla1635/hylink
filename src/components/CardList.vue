<template>
  <v-layout column id="container">
    <v-layout>
      <v-flex v-if="sharing_flag" style="font-size:18px; font-weight:bold;">현재 선택된 카드 수 {{selectedCard.length}} <v-btn @click="sharing" icon><v-icon>done_outline</v-icon></v-btn></v-flex>
      <v-spacer/>
      <v-btn @click="sharing_flag=!sharing_flag" icon><v-icon>share</v-icon></v-btn>
      <v-menu transition="slide-y-transition" :close-on-content-click="false">
        <template v-slot:activator="{ on }">
          <v-btn icon><v-icon style="width:40px; height:40px;"  v-on="on">apps</v-icon> </v-btn>
        </template>
        <v-list style="padding:0px 10px;">
          <div style="margin:5px;text-align:center;">Option</div>
          <v-divider/>
          <div>
            <v-switch
              class="switch"
              color="primary"
              v-model="thumnail_flag" 
              inset
              :label="`썸네일`"
              style="margin-top:5px;"
            />
            <v-switch
              color="primary"
              v-model="summary_flag" 
              inset
              :label="`요약`"
              style="margin:0px;"
            />
          </div>
          </v-list>
    </v-menu>
    </v-layout>
      <v-item-group multiple v-model="selectedCard">
        <v-layout  row wrap >
            <v-flex v-for="(item, index) in cardList" :key="index" xs12 sm6 lg6 xl6 >
              <Card :card="item" :index="index" :thumnail_flag="thumnail_flag" :summary_flag="summary_flag" :sharing_flag="sharing_flag"/>
            </v-flex>
        </v-layout>
      </v-item-group>
  </v-layout>
</template>

<script>
/* eslint-disable no-console */

import Card from '@/components/Card'
 
export default {
  name: 'CardList',
  data() {
    return{
      thumnail_flag:true,
      summary_flag:true,
      sharing_flag:false,
      selectedCard:[],
      card_num:0
    }
  },
  components: {
    Card
  },
  props: {
    cardList: {type:Array}
  },
  watch: {
      selectedCard: function() {
        console.log(this.selectedCard)
      }
  },
  methods: {
    updateCardNum(event) {
      this.card_num= event
    },
    sharing() {
      var card_id = []
      this.cardList.forEach((element, index) => {
        if(this.selectedCard[0]===index) {
          card_id.push(element.id)
          this.selectedCard.splice(0, 1)
        }
      });

      console.log(card_id)

      const payload= {
        link_list: card_id
      }

      this.$store.dispatch("shareCard", payload)
      this.sharing_flag=false
    }
  }
}
</script>

<style>
/* switch태그의 불필요한 요소 제거 */
.v-input__control .v-messages {
  display: none;
} 
</style>

<style scoped>
.switch {
  margin:0px;
}
#container {
  padding:0 10%;
}
</style>
