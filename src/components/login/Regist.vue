<template>
    <v-card flat width="300" color="#ffffff00">
        <v-toolbar flat borderless color="#ffffff00">
            <v-container>
                <v-row justify="center" class="display-3">
                    <v-img alt="Logo" src="@/assets/link.png" max-width="50" max-height="500"></v-img>
                    HyLink
                </v-row>
            </v-container>

        </v-toolbar>

        <v-container>
            <v-row justify="center">
                <v-img src="https://source.unsplash.com/random" max-width="100" height="100" class="img-circle">
                </v-img>
            </v-row>
            
            <v-row justify="center">

                <v-form>
                    <v-container grid-list-md text-xs-center>
                        <v-text-field 
                            class="input-with-icon form_input" 
                            name='username' 
                            label='Username' 
                            v-model='credentials.username' 
                            type='text' 
                            prepend-icon="face" 
                            required></v-text-field>
                        <v-text-field 
                            class="input-with-icon form_input" 
                            name='email' 
                            label='E-Mail' 
                            v-model='credentials.email' 
                            type='email' 
                            prepend-icon="mail_outline" 
                            required></v-text-field>
                        <v-text-field 
                            class="input-with-icon form_input" 
                            name='password' 
                            label='Password' 
                            v-model='credentials.password' 
                            type='password' 
                            prepend-icon="lock" 
                            required></v-text-field>
                        <!-- <v-text-field 
                            class="input-with-icon form_input" 
                            name='confirmPassword' 
                            label='confirmPassword' 
                            v-model='confirmPassword' 
                            type='password' 
                            prepend-icon="check_circle" 
                            required></v-text-field> -->
                    </v-container>
                </v-form>

            </v-row>

            <v-row justify="center" width="200">
                <v-btn rounded color="#B5D4B8">Back</v-btn>
                <v-spacer></v-spacer>
                <v-btn 
                    rounded 
                    color="#B6DCCC"
                    @click="signUp">Sign Up</v-btn>
            </v-row>
        </v-container>

    </v-card>
</template>

<script>

export default {
    name: 'regist',
    props: {
        source: String,
    },
    data: () => ({
        credentials: {
            'username': "",
            'email': "",
            'password': "",
        },
        // confirmPassword: null,
    }),
    methods: {
        signUp: function() {
            this.$axios.post('http://127.0.0.1:8000/api/users/', this.credentials)
                .then(res => {
                    this.$swal('회원가입 성공', '환영합니다!', 'OK')
                    this.router.push({
                        name: 'login'
                    });
                    // eslint-disable-next-line no-console
                    console.log(res)
                })
                .catch(() => {
                    this.$swal({
                        type: 'error',
                        title: 'Oops...',
                        text: '아이디, 이메일, 비밀번호를 확인해주세요!',
                        showCloseButton:true,
                    })
                })
        }
    } 
}
</script>

<style scoped>
.img-circle {
    border-radius: 50%;
}

.form_input {
    width: 300px;
}
</style>
