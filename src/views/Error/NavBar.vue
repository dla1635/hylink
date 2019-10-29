<template>
<v-navigation-drawer fixed clipped class="grey lighten-4" app>
    <v-list dense class="grey lighten-4">
        <template v-for="(item, i) in items">
            <v-row v-if="item.heading" :key="i" align="center">
                <v-col cols="6">
                    <v-subheader v-if="item.heading">
                        {{ item.heading }}
                    </v-subheader>
                </v-col>
                <v-col cols="6" class="text-right">
                    <v-btn small text>edit</v-btn>
                </v-col>
            </v-row>
            <v-divider v-else-if="item.divider" :key="i" dark class="my-4"></v-divider>
            <v-list-item v-else :key="i" @click="drawer">
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
</template>

<script>

export default {
    name: "NavBar",
    data() {
        return {
            items: [{
                    heading: 'Labels'
                },
                {
                    divider: true
                },
                {
                    icon: 'local_offer',
                    text: 'Algorithm'
                },
                {
                    icon: 'local_offer',
                    text: 'BigData'
                },
                {
                    icon: 'local_offer',
                    text: 'BlockChain'
                },
                {
                    icon: 'local_offer',
                    text: 'AI'
                },
                {
                    icon: 'local_offer',
                    text: 'jAVA'
                }
            ]
        }
    }
}
</script>
