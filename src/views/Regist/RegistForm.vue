<template>
<v-card flat width="300" color="#ffffff00">
    <v-toolbar flat borderless color="#ffffff00">
        <v-container>
            <v-row justify="center" class="display-3">
                <v-img alt="Logo" src="@/assets/link.png" max-width="50" max-height="500" contain></v-img>
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

                    <v-text-field class="input-with-icon form_input" name='email' label='E-Mail' v-model='inputs.email' type='email' prepend-icon="mail_outline" required></v-text-field>
                    <v-text-field class="input-with-icon form_input" name='username' label='UserName' v-model='inputs.username' type='text' prepend-icon="face" required></v-text-field>
                    <v-text-field class="input-with-icon form_input" name='password1' label='Password' v-model='inputs.password1' type='password' prepend-icon="lock" required></v-text-field>
                    <v-text-field class="input-with-icon form_input" name='password2' label='confirmPassword' v-model='inputs.password2' type='password' prepend-icon="check_circle" required></v-text-field>
                </v-container>
            </v-form>

        </v-row>

        <v-row justify="center" width="200">
                <v-btn rounded color="#B5D4B8">Back</v-btn>
                <v-spacer></v-spacer>
                <v-btn rounded color="#B6DCCC" @click="createAccount(inputs)">Sign Up</v-btn>

        </v-row>
    </v-container>

</v-card>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
    name: 'RegistForm',
    props: {
        source: String,
    },
    data: () => ({
        drawer: null,
        inputs: {
            username: '',
            password1: '',
            password2: '',
            email: '',
        }
    }),
    computed: mapState('signup', [
        'registrationCompleted',
        'registrationError',
        'registrationLoading',
    ]),
    methods: mapActions('signup', [
        'createAccount',
        'clearRegistrationStatus',
        'activateAccount',
    ]),
    beforeRouteLeave(to, from, next) {
        this.clearRegistrationStatus();
        next();
    },
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
