<template>
<v-container>
    <!-- 상단 바 -->
    <AppBar></AppBar>

    <v-layout text-center wrap>
        <v-flex xs12>
            <v-img :src="require('@/assets/logo.svg')" class="my-3" contain height="200"></v-img>
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
import AppBar from './AppBar'

export default {
    name: 'WelcomePage',
    components: {
        AppBar,
    },
    data() {
        return {
        }
    },

};
</script>
