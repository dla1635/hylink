<template>
  <v-app id="container">
    <v-container fluid>
        <CardList :cardList="card_list"/>
    </v-container>
  </v-app>
</template>

<script>
import CardList from '@/components/CardList'
import {mapStore, mapState} from '@/'

export default {
  name: "HomePage",
  components: {
      CardList
  },
  data() {
    return {
      card_list : [],
    };
  },
  mounted() {

  },
  methods: {
  }
};
</script>

<style scoped>
#container {
    background-color: white;
}

</style>
