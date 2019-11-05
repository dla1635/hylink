<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Card Info</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
                <v-img width=""  :src="thumbnail"></v-img>
              <v-col cols="12">
                <v-text-field label="title*" required v-model="title"></v-text-field>
              </v-col>

              <v-col cols="12">
                  <v-textarea label="summary" v-model="summary"></v-textarea>
              </v-col>

              <v-col cols="12">
                <v-combobox
                    v-model="selectedLabels"
                    :items="labelList"
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
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="dialog = false">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
/* eslint-disable */
export default {
    data: () => ({
        dialog: true,
        title:"",
        summary:"",
        tag:[],
        label:[],
        thumbnail:"",
        selectedLabels:[],
        selectedTags:[]
    }),
    props: {
        card: {type:Object}
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
    }
}
</script>