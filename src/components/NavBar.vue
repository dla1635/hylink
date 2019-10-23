<template>
    <v-app>
      <v-navigation-drawer
      v-model="drawer"
      fixed
      clipped
      class="grey lighten-4"
      app
      >
      <v-list
        dense
        class="grey lighten-4"
      >
        <template v-for="(item, i) in items">
          <v-row
            v-if="item.heading"
            :key="i"
            align="center"
          >
            <v-col cols="6">
              <v-subheader v-if="item.heading">
                {{ item.heading }}
              </v-subheader>
            </v-col>
            <v-col
              cols="6"
              class="text-right"
            >
              <v-btn
                small
                text
              >edit</v-btn>
            </v-col>
          </v-row>
          <v-divider
            v-else-if="item.divider"
            :key="i"
            dark
            class="my-4"
          ></v-divider>
          <v-list-item
            v-else
            :key="i"
<<<<<<< HEAD
=======
            @click="drawer"
>>>>>>> 23299980eae983c98c0ee1dd0ce6e59119e6215a
          >
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="grey--text">
                {{ item.text }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>
    
    <v-app-bar
      app
      clipped-left
      color="amber"
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <span class="title ml-3 mr-5">Google&nbsp;<span class="font-weight-light">Keep</span></span>
      <v-text-field
        text
        hide-details
        prepend-inner-icon="search"
      ></v-text-field>
      <v-flex align-center>
        <v-btn icon>
        <img src="https://www.w3schools.com/css/paris.jpg" 
          style="width:50px; height:50px; border-radius: 50%;"/>
        </v-btn>
        <span style="font-size:20px; line-height:24px;">종완띠</span>
      </v-flex>
    </v-app-bar>

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