<template>
  <v-layout row wrap>
    <v-flex xs6 sm6 lg6 xl6 v-for="(item, index) in cardList" :key="index" @click="resizeCard(index)">
      <Card :card="item"/>
    </v-flex>
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
    resizeCard(index) {
          console.log("들어옴")
          var card = document.querySelector(".card")
          card.setAttribute("style", "height:300px")
    },
  }
}
</script>

<style scoped>
</style>
