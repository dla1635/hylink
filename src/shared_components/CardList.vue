<template>
  <v-layout column id="container">
    <v-layout>
      <v-text-field
          solo
          text
          hide-details
          label="URL"
          prepend-inner-icon="link"
          style="width:300px; margin-bottom:10px;"
      ></v-text-field>
      <v-spacer/>
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
    <v-layout  row wrap >
      <v-flex v-for="(item, index) in cardList" :key="index" xs12 sm6 lg6 xl6 >
        <Card :card="item" :index="index" :thumnail_flag="thumnail_flag" :summary_flag="summary_flag"/>
      </v-flex>
    </v-layout>

  </v-layout>
</template>

<script>
import Card from '@/shared_components/Card'
 
export default {
  name: 'CardList',
  data() {
    return{
      thumnail_flag:true,
      summary_flag:true,
    }
  },
  components: {
    Card
  },
  props: {
    cardList: {type:Array}
  },
  methods: {
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
