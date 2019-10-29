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
                <v-form ref="form" v-model="valid" lazy-validation>
                    <v-text-field 
                        v-model="credentials.username"
                        :counter="70"
                        label="username"
                        id="username" 
                        :rules="rules.username"
                        maxlength="70"
                        required

                        class="form_input" 
                        background-color="#C8EBCC" 
                        name="username" 
                        prepend-icon="person" 
                        type="text" 
                        outlined
                        rounded
                        single-line
                        loading="false" 
                        dense></v-text-field>
                    <v-text-field 
                        type="password"
                        v-model="credentials.password"
                        :counter="20"
                        label="password"
                        id="password" 
                        :rules="rules.password"
                        maxlength="20"
                        required

                        class="form_input" 
                        background-color="#C8EBCC" 
                        name="password" 
                        prepend-icon="lock" 
                        outlined
                        rounded
                        single-line
                        loading="false" 
                        dense></v-text-field>
                    <p class="caption ma-0">Forgot password?</p>
                </v-form>
            </v-row>
            

        </v-container>
    </v-card-text>

    <v-card-actions>
        <v-container>
            <v-row justify="center">
                <v-btn 
                    color="#B6DCCC" 
                    rounded
                    width="100" 
                    height="25"
                    :disabled="!valid" 
                    @click="login">Login</v-btn>
            </v-row>

        </v-container>
    </v-card-actions>
</v-card>
</template>

<script>
export default {
    name: 'login',
    props: {
    },
    data: () => ({
        credentials: {
          'username': "",
          'password': "",
        },
        valid: true,
        rules: {
          username: [
            v => !!v || "Username is required",
            v => (v && v.length > 3) || "A username must be more than 3 characters long",
            v => /^[a-z0-9_]+$/.test(v) || "A username can only contain letters and digits"
          ],
          password: [
            v => !!v || "Password is required",
            v => (v && v.length > 7) || "The password must be longer than 7 characters"
          ]
        },
    }),

    methods: {
        login: function() {
          // checking if the input is valid
          if (this.$refs.form.validate()) {
              this.loading = true;
              this.$axios.post('http://localhost:8000/api/auth/', this.credentials).then(res => {
              this.$session.start();
              this.$session.set('token', res.data.token);
              this.$router.push('/');
              // eslint-disable-next-line no-console
              console.log(res)
            }).catch(() => {
              this.$swal({
                type: 'warning',
                title: 'Error',
                text: 'Wrong username or password',
                showConfirmButton:false,
                showCloseButton:true,
                timer:3000
              })
            })
          }
        }
    }
}
</script>

<style scoped>
.form_input {
    width: 300px;
}