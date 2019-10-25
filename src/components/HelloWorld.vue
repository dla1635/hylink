<template>
<v-container>
    <v-layout text-center wrap>
        <v-flex xs12>
            <v-img :src="require('../assets/logo.svg')" class="my-3" contain height="200"></v-img>
        </v-flex>

        <v-flex mb-4>
            <h1 class="display-2 font-weight-bold mb-3">
                로그인, 회원가입 테스트 페이지
            </h1>

        </v-flex>

        <v-flex xs12 mb-5>
            <h2 class="headline font-weight-bold mb-3">메뉴</h2>

            <v-layout justify-center>
                <router-link to="login"> 로그인 </router-link>

            </v-layout>
            <v-layout justify-center>
                <router-link to="regist"> 회원가입 </router-link>
            </v-layout>

        </v-flex>
    </v-layout>

</v-container>
</template>

<script>
export default {
    data: () => ({
        ecosystem: [{
                text: 'vuetify-loader',
                href: 'https://github.com/vuetifyjs/vuetify-loader',
            },
            {
                text: 'github',
                href: 'https://github.com/vuetifyjs/vuetify',
            },
            {
                text: 'awesome-vuetify',
                href: 'https://github.com/vuetifyjs/awesome-vuetify',
            },
        ],
        importantLinks: [{
                text: 'Documentation',
                href: 'https://vuetifyjs.com',
            },
            {
                text: 'Chat',
                href: 'https://community.vuetifyjs.com',
            },
            {
                text: 'Made with Vuetify',
                href: 'https://madewithvuejs.com/vuetify',
            },
            {
                text: 'Twitter',
                href: 'https://twitter.com/vuetifyjs',
            },
            {
                text: 'Articles',
                href: 'https://medium.com/vuetify',
            },
        ],
        whatsNext: [{
                text: 'Explore components',
                href: 'https://vuetifyjs.com/components/api-explorer',
            },
            {
                text: 'Select a layout',
                href: 'https://vuetifyjs.com/layout/pre-defined',
            },
            {
                text: 'Frequently Asked Questions',
                href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
            },
        ],
    }),
};
</script>
