
<template>
<v-hover v-slot:default="{ hover }">
  <v-card class="card" :elevation="hover ? 12 : 2" :color="hover ? '#F2F2F2': '#fff'">
    <v-layout class="card_sub1">
      <v-flex class="card_sub2">
        <v-layout>
          <v-flex  xs9 sm9 lg9 xl9>
            <input v-if="editFlag" type="text" v-model="card.title">
            <span v-if="!editFlag" style="font-size:20px;" @click="goLink">{{card.title}}</span><br/>
          </v-flex>
            <div style="display:inline-block; height:0px;" v-show="hover"  xs3 sm3 lg3 xl3>
              <v-btn icon @click="changeEditMode"><v-icon size=20>edit</v-icon></v-btn>
              <v-btn icon @click="copyToClipboard(card.url)"><v-icon size=20>file_copy</v-icon></v-btn>
            </div>
        </v-layout>
        <v-flex v-show="summary_flag">
          <v-textarea v-if="editFlag" dense rows="3" cols="38" v-model="card.summary"></v-textarea>
          <!-- <input v-if="editFlag" type="text" v-model="card.summary"> -->
          <p v-if="!editFlag" class="summary">{{card.summary}}</p>
        </v-flex>
      </v-flex>
      <img v-show="thumnail_flag" class="card_img" :src="card.thumbnail" />
    </v-layout>
        <v-flex id="tagContainer">
          <span class="tag"  style="font-size:70%; height:26px; margin:7px; padding:0 0px;" v-for="tag in card.tagList" :key="tag">#{{tag}}</span>
        </v-flex>
  </v-card>
  </v-hover>
</template>

<script>
export default {
  name: "Card",
  data() {
    return{
      editFlag: false,
    }
  },
  props: {
    card: { type: Object },
    index: { type: Number },
    thumnail_flag: { type: Boolean},
    summary_flag: { type: Boolean},
  },
  methods: {
    goLink() {
      location= this.card.url;
    },
    changeEditMode() {
      this.editFlag?this.editFlag=false:this.editFlag=true;
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
.card {
  margin: 10px 10px;
  column-width: 300px;
  height:143px;
}

.card_sub1 {
}
.card_sub2 {
  padding:5px 0 0 5px;
}
.card_img {
  width: 100px;
  height: 100px;
}
.tag {
  font-size: 70%;
  height:25px; 
  margin:5px 7px 0 0; 
  padding:0 0px;
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
