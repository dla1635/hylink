<template>
    <section id="contact-us">
        <v-container grid-list-md>
          <v-layout row wrap justify-center>
                <v-flex xs12 text-center class="mt-5">
                    <div class="headline">Are you amazed? Stay tuned!</div>
                    <br>
                    <div>궁금하신 점이 있으면 언제든 저희에게 연락주세요!</div>
                </v-flex>
                <v-flex xs8  style="max-width: 500px;">
                    <v-card class="elevation-0 transparent">
                        <v-card-text>
                            <v-flex xs12>
                                <v-text-field box label="Email address" :rules="emailRules" v-model="email" hint="Enter your email!" persistent-hint></v-text-field>
                            </v-flex>
                            <v-flex xs12>
                                <v-text-field box multi-line v-model="contents" label="Bio and curiosities"></v-text-field>
                            </v-flex>
                            <v-flex xs12 class="text-center">
                                <v-btn class="blue lighten-2 mb-5" dark large @click="subscribe">Get in touch</v-btn>
                            </v-flex>
                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </section>
</template>

<script>
export default {
    name: 'ContactUs',
    data: () => {
        return {
            email: "",
            contents: "",
            emailRules: [
                v => {
                return !!v || "E-mail is required";
                },
                v =>
                /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
                "E-mail must be valid"
            ],
        }
    },
    methods: {
        subscribe: () => {
            // 이메일 api를 이용해 이메일 보내는 기능 
        }
    }
}
</script>
<style lang="stylus">
#contact-us {
    margin-top: 50px;
    margin-bottom: 100px;
}
</style>