<template>
  <v-layout column id="container">
    <v-text-field
        solo
        text
        hide-details
        label="Search"
        prepend-inner-icon="search"
        style="width:300px;"
    ></v-text-field>
    <v-layout  row wrap>
      <v-flex v-for="(item, index) in cardList" :key="index" xs12 sm6 lg6 xl6 >
        <Card :card="item" :index="index"/>
      </v-flex>
    </v-layout>
  </v-layout>
</template>

<script>
import Card from '@/components/Card'
 
export default {
  name: 'CardList',
  components: {
    Card
  },
  props: {
    cardList: {type:Array}
  },
  methods: {
    // resizeCard(index) {
    //       console.log("들어옴",index)
    //       var card = document.querySelectorAll(".card")
    //       console.log(card.length)
    //       for(var i = 0 ;i < card.length;i++) {
    //         if(card)
    //       }
    //       card[index].setAttribute("style", "height:300px")
    // },
  }
}
</script>

<style scoped>

#container {
  padding:0 10%;
}
</style>
