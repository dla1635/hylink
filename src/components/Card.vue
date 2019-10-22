<template>
<v-expand-transition>
  <v-card class="card" @click="expandDetail(index)">
    <v-layout>
      <v-flex class="card_detail">
        <span style="font-size:20px;">{{card.title}}</span><br/>
        <span class="summary">책상이나 바닥처럼 평평한 곳 어디에서든 무선으로 전자기기를 충전할 수 있는 기술이 나왔다.기존의 무선 충전 기술은 공기를 이용해 전력을 주고받는 자기장 신호를 전달해 충전한다.연구팀은 실험과 시뮬레이션을 통해 실제로 이 무선충전 시스템이 기존 방식보다 훨씬 효율적으로 충전할 수 있음을 확인했다.</span>
      <span class="tag" v-for="tag in card.tagList" :key="tag">#{{tag}}</span>
      </v-flex>
      <img class="card_img" :src="card.thumbnail" />
    </v-layout>
  </v-card>
  </v-expand-transition>
</template>

<script>
export default {
  name: "Card",
  props: {
    card: { type: Object },
    index: { type: Number }
  },
  methods: {
    expandDetail(index) {
      var a = document.querySelectorAll(".summary")[index];

      if (a.style.display === "none") {
        a.setAttribute("style", "display:block");
        return;
      }

      a.setAttribute("style", "display:none");
    }
  },
  mounted() {
    var arrow = document.querySelectorAll(".v-list-item__icon");
    arrow.forEach(item => {
      item.remove();
    });
    var margin = document.querySelectorAll(".v-list-group__header");
    margin.forEach(item => {
      item.setAttribute("padding", "0");
    });
  }
};
</script>

<style scoped>
.card {
  margin: 5px 10px;
  transition: height 1s linear; 
}

.card_detail {
  padding: 10px;
}
.card_img {
  width: 100px;
  height: 100px;
}
.tag {
  margin-right: 5px;
}

v-list-item__icon v-list-group__header__append-icon {
  display: none;
}

.summary {
    margin: 5px 0;
    color:#000; 
    display:none;
    font-size: 13px;
}
</style>
