<template>
  <v-card class="card" style="column-width: 300px;">
    <v-layout>
      <v-flex class="card_detail">
        <v-flex>
          <span style="font-size:20px;">{{card.title}}</span><br/>
        </v-flex>
        <v-flex>
          <p class="summary">{{card.summary}}</p>
        </v-flex>
      </v-flex>
      <img class="card_img" :src="card.thumbnail" />
    </v-layout>
        <v-flex>
          <v-btn outlined class="tag"  style="font-size: 70%; height:26px; margin:7px; padding:0 0px;" v-for="tag in card.tagList" :key="tag" >#{{tag}}</v-btn>
        </v-flex>
  </v-card>
</template>

<script>
export default {
  name: "Card",
  props: {
    card: { type: Object },
    index: { type: Number }
  },
  methods: {
  },
  mounted() {
    // var arrow = document.querySelectorAll(".v-list-item__icon");
    // arrow.forEach(item => {
    //   item.remove();
    // });
    // var margin = document.querySelectorAll(".v-list-group__header");
    // margin.forEach(item => {
    //   item.setAttribute("padding", "0");
    // });
  }
};
</script>

<style scoped>
.card {
  margin: 5px 10px;
  column-width: 300px;
}

.card_detail {
  padding: 5px;
}
.card_img {
  width: 100px;
  height: 100px;
}
.tag {
  font-size: 5px;
  height:25px; 
  margin:5px 7px 0 0; 
  padding:0 0px;
}

/* v-list-item__icon v-list-group__header__append-icon {
  display: none;
} */

.summary {
    margin: 5px 0;
    color:rgba(3, 3, 3, 0.527); 
    font-size: 13px;
    max-height:99px; 
    min-height:0px;
    display: -webkit-box; 
    display: -ms-flexbox; 
    display: box; 
    margin-top:1px; 
    overflow:hidden; 
    vertical-align:top; 
    text-overflow: ellipsis; 
    word-break:break-all; 
    -webkit-box-orient:vertical; 
    -webkit-line-clamp:4
}
</style>
