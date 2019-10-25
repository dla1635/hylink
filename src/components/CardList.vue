<template>
  <div id="container">
    <div>
    <v-text-field
        solo
        text
        hide-details
        label="URL"
        prepend-inner-icon="link"
        style="width:300px;"
    ></v-text-field>
    </div>
    <!-- <v-layout  row wrap style="column-width:350px; column-gap: 15px;">
      <v-flex v-for="(item, index) in cardList" :key="index" xs12 sm6 lg6 xl6 >
        <Card :card="item" :index="index"/>
      </v-flex>
    </v-layout> -->
    <template v-for="(item, index) in cardList"  xs12 sm6 lg6 xl6 >
        <Card :card="item" :index="index" :key="index"/>
    </template>
  </div>
   <!-- <div id="columns">
      <template v-for="(item, index) in imgList"  xs12 sm6 lg6 xl6 >
        <figure :key="index">
          <img :src="item">
          <figcaption>Cinderella wearing European fashion of the mid-1860’s</figcaption>
        </figure>
      </template>
    </div> -->
</template>

<script>
import Card from '@/components/Card'
 
export default {
  name: 'CardList',
  data() {
    return{
      imgList: ["//s3-us-west-2.amazonaws.com/s.cdpn.io/4273/cinderella.jpg",
      "//s3-us-west-2.amazonaws.com/s.cdpn.io/4273/rapunzel.jpg",
      "//s3-us-west-2.amazonaws.com/s.cdpn.io/4273/belle.jpg",
      "//s3-us-west-2.amazonaws.com/s.cdpn.io/4273/mulan_2.jpg",
      "//s3-us-west-2.amazonaws.com/s.cdpn.io/4273/sleeping-beauty.jpg"
      ]
    }
  },
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
  column-width:350px;
  column-gap: 15px;
}

#columns{
        column-width:350px;
        column-gap: 15px;
      }
      #columns figure{
        display: inline-block;
        border:1px solid rgba(0,0,0,0.2);
        margin:0;
        margin-bottom: 15px;
        padding:10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.5);;
      }
      #columns figure img{
        width:100%;
      }
      #columns figure figcaption{
        border-top:1px solid rgba(0,0,0,0.2);
        padding:10px;
        margin-top:11px;
      }
</style>
