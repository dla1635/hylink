<template>
<v-hover v-slot:default="{ hover }">
  <v-card class="card" :elevation="hover ? 5 : 2">
    <CardModifyModal v-if="modal_flag" :card="card"></CardModifyModal>
    <div
      v-if="hover"
      class="d-flex v-card--reveal display-3"
      style="height: 100%;  background-color:#0002;"
    >
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
           <v-btn class="mr-3" icon @click="goLink" v-on="on"><v-icon size=20>reply</v-icon></v-btn>
        </template>
        <span>링크 이동</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
           <v-btn class="mr-3" icon @click="changeEditMode" v-on="on"><v-icon size=20>edit</v-icon></v-btn>
        </template>
        <span>편집</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
           <v-btn  icon @click="copyToClipboard(card.url)" v-on="on"><v-icon size=20>file_copy</v-icon></v-btn>
        </template>
        <span>클립보드 복사</span>
      </v-tooltip>
    </div>
      <v-layout class="card_sub1">
        <v-flex class="card_sub2">
          <v-layout>
            <p id="card_title" v-if="!editFlag" style="font-size:20px;">{{card.title}}</p><br/>
          </v-layout>
          <v-flex v-show="summary_flag">
            <p v-if="!editFlag" class="summary">{{card.summary}}</p>
          </v-flex>
        </v-flex>
        <img v-show="thumnail_flag" class="card_img" :src="card.thumbnail" />
      </v-layout>
      <v-flex id="tagContainer">
        <v-chip class="tag"  v-for="tag in card.tagList" :key="tag">#{{tag}} </v-chip>
      </v-flex>
  </v-card>
  </v-hover>
</template>

<script>
import CardModifyModal from '@/components/CardModifyModal'

export default {
  name: "Card",
  data() {
    return{
      editFlag: false,
      modal_flag: false,
    }
  },
  props: {
    card: { type: Object },
    index: { type: Number },
    thumnail_flag: { type: Boolean},
    summary_flag: { type: Boolean},
  },
  components: {
    CardModifyModal
  },
  methods: {
    goLink() {
      location= this.card.url;
    },
    changeEditMode() {
      this.modal_flag?this.modal_flag=false:this.modal_flag=true;
    },
    copyToClipboard(val) {
      var t = document.createElement("textarea");
      document.body.appendChild(t);
      t.value = val;
      t.select();
      document.execCommand('copy');
      document.body.removeChild(t);
      alert("클립보드에 복사 했습니다.")
    }
  },
  mounted() {
  }
};
</script>

<style scoped>

.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  position: absolute;
  width: 100%;
  z-index: 10;
}

.card {
  margin: 10px 10px;
}
.card_sub1 {
}
.card_sub2 {
  padding:5px 0 0 5px;
}

#card_content {
  position: relative;
  top:0px;
}

#card_title {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 150px;
  height: 30px;
  margin:0px;
}
.card_img {
  width: 100px;
  height: 100px;
}
.tag {
  margin:7px; 
  }

.summary {
    margin: 0px;
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
    -webkit-line-clamp:3;
    line-height:21px;
}

#tagContainer {
  margin-top: 5px;
}
</style>
