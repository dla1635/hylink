<template>
<v-card flat width="500" color="#ffffff00">
    <v-toolbar flat borderless height="200" color="#ffffff00">
        <v-container>
            <v-row justify="center" class="display-4">HyLink</v-row>
        </v-container>
    </v-toolbar>

    <v-card-text class="pb-0">
        <v-container>
            <v-row justify="center">
                <v-form>
                    <v-text-field class="form_input" 
                                  background-color="#C8EBCC" 
                                  label="Email" 
                                  id="email" 
                                  name="email" 
                                  v-model="inputs.email"
                                  prepend-icon="person" 
                                  type="text" 
                                  outlined
                                  rounded
                                  single-line
                                  loading=false
                                  dense></v-text-field>
                    <v-text-field class="form_input" 
                                  background-color="#C8EBCC" 
                                  label="Password" 
                                  id="password" 
                                  name="password" 
                                  v-model="inputs.password"
                                  prepend-icon="lock" 
                                  type="password" 
                                  outlined
                                  rounded
                                  single-line
                                  loading=false
                                  dense></v-text-field>
                    <p class="caption ma-0">Forgot password?</p>
                </v-form>
            </v-row>
            

        </v-container>
    </v-card-text>

    <v-card-actions>
        <v-container>
            <v-flex col-xs-12 justify-center text-center>
                <v-btn 
                color="#B6DCCC" 
                rounded 
                width="100" 
                height="25"
                @click="login(inputs)">Login</v-btn>
            </v-flex>
        </v-container>
    </v-card-actions>
</v-card>
</template>

<script>
/* eslint-disable no-console */
export default {
    name: 'LoginForm',
    data() {
        return {
            drawer: null,
            inputs: {
                email: '',
                password: '',
            },
        }
    },
    methods: {
        login({ email, password }) {
            console.log(email, password)
            this.$store.dispatch('auth/login', { email, password })
                .then(() =>
                    this.$router.push('/home'));
        },
    }
}
</script>

<style scoped>
.form_input {
    width: 300px;
}
