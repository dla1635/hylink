<template>
    <v-app>
      <v-navigation-drawer
      v-model="drawer"
      fixed
      clipped
      class="grey lighten-4"
      app
      >
      <v-list dense class="grey lighten-4">
        <template v-for="(item, i) in items">
          <v-layout
            v-if="item.heading"
            :key="i"
            row
            align-center
          >
            <v-flex xs6>
              <v-subheader v-if="item.heading">
                {{ item.heading }}
              </v-subheader>
            </v-flex>
            <v-flex xs6 class="text-xs-right">
              <v-btn small flat>edit</v-btn>
            </v-flex>
          </v-layout>

          <v-divider
            v-else-if="item.divider"
            :key="i"
            dark
            class="my-3"
          ></v-divider>

          <v-list-tile
            v-else
            :key="i"
            @click=""
          >
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>

            <v-list-tile-content>
              <v-list-tile-title class="grey--text">
                {{ item.text }}
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
    </v-navigation-drawer>
    
    <v-toolbar color="amber" app   clipped-left>
      <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon>
      <span class="title ml-3 mr-5">Google&nbsp;<span class="font-weight-light">Keep</span></span>
      <v-text-field
        solo-inverted
        flat
        hide-details
        label="Search"
        prepend-inner-icon="search"
      ></v-text-field>
      <v-spacer></v-spacer>
    </v-toolbar>

    <!-- 라우터뷰  -->
    <v-content><router-view/></v-content>
    </v-app>
</template>

<script>
export default {
    name:"navBar",
    data() {
        return{
            drawer: null,
        items: [
            { heading: 'Labels' },
            { divider: true },
            { icon: 'local_offer', text: 'Algorithm' },
            { icon: 'local_offer', text: 'BigData' },
            { icon: 'local_offer', text: 'BlockChain' },
            { icon: 'local_offer', text: 'AI' },
            { icon: 'local_offer', text: 'jAVA' }
        ]
        }
    }
}
</script>

<style lang="stylus">
  #keep
    .v-navigation-drawer__border
      display: none
</style>