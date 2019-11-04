<template>
<v-navigation-drawer fixed clipped class="grey lighten-4" app>
    <v-list dense class="grey lighten-4">
      <v-row  align="center">
          <v-col cols="6">
            <v-subheader>
                Labels
            </v-subheader>
          </v-col>
      </v-row>
      <v-divider  dark class="my-4"/>
      <template v-for="(item, i) in labels">
        <v-list-item :key="i" >
            <v-list-item-action>
                <v-icon>local_offer</v-icon>
            </v-list-item-action>
            <v-list-item-content>
                <v-list-item-title class="grey--text" @click="moveToLabel(item.name)">
                    {{ item.name }}
                </v-list-item-title>
            </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
</v-navigation-drawer>
</template>

<script>
/* eslint-disable */
/* eslint-disable no-console */
import {mapActions} from 'vuex'
import Store from '@/vuex/store'

export default {
    name: "NavBar",
    data() {
        return {
          labels:[]
        }
    },
    methods: {
      ...mapActions({
            getLabels: 'getLabels'
        }),
        moveToLabel(content) {
          // catch문 => dupalate Component error 해결
          this.$router.push({name:'home', params: { type:"label", content: content }}).catch(err => {})
        }
    },
    async mounted() {
      await this.getLabels()
      this.labels = Store.state.layout.labels

    }
}
</script>
