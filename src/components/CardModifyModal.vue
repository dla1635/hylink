<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Card Info</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
                <v-img style="width:200px; height:200px;" :src="thumbnail"></v-img>
              <v-col cols="12">
                <v-text-field label="title*" required v-model="title"></v-text-field>
              </v-col>

              <v-col cols="12">
                  <v-textarea label="summary" v-model="summary"></v-textarea>
              </v-col>

              <v-col cols="12">
                <v-combobox
                    v-model="selectedLabels"
                    :items="label"
                    label="Label"
                    multiple
                    chips
                ></v-combobox>
              </v-col>

              <v-col cols="12">
                <v-combobox
                    v-model="selectedTags"
                    :items="tag"
                    label="Tag"
                    multiple
                    chips
                ></v-combobox>
              </v-col>

            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="remove">제거</v-btn>
          <v-btn color="blue darken-1" text @click="modify">저장</v-btn>
          <v-btn color="blue darken-1" text @click="dialog = false">취소</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
/* eslint-disable */
import Store from '@/vuex/store'

export default {
    data: () => ({
        dialog: true,
        title:"",
        summary:"",
        selectedLabels:[],
        selectedTags:[],
        thumbnail:"",
        tag:[],
        label:[],
    }),
    props: {
        card: {type:Object}
    },
    methods: {
      async modify() {

        const payload = {
          'token': localStorage.getItem('TOKEN_STORAGE_KEY'),
          l_id: this.card.id,
          title: this.title,
          tags : this.selectedTags,
          labels : this.selectedLabels,
          thumbnail : this.thumbnail,
          summary : this.summary,
          is_visible : 3,
        }
        // const config = {
        //         headers: {
        //             'token': localStorage.getItem('TOKEN_STORAGE_KEY')
        //         }
        // }
        var res = await this.$store.dispatch("setCard", payload);

        alert('수정사항이 저장되었습니다.')
        this.dialog = false
      },
      async remove() {
        const payload = {
          l_id: this.card.id,
          del: "delete"
        }
        const config = {
                headers: {
                    'token': localStorage.getItem('TOKEN_STORAGE_KEY')
                }
        }
        var res = await Store.dispatch("deleteCard", payload, config);

        alert('링크가 삭제 되었습니다.')
        this.dialog = false
      }
    },
    mounted(){
        this.title = this.card.title;
        this.summary = this.card.summary;
        this.thumbnail = this.card.thumbnail;
        this.tag = this.card.tag.map(element => {
          return element.name
        });
        console.log(this.tag)
        this.label = this.card.label.map(element => {
          return element.name
        });
        console.log(this.card)
        console.log(this.label)

    }
}
</script>