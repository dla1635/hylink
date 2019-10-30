<template>
<v-card flat width="300" color="#ffffff00">
    <v-toolbar flat borderless color="#ffffff00">
        <v-container>
            <v-row justify="center" class="display-3">
                <v-img alt="Logo" src="@/assets/link.png" max-width="50" max-height="500" contain="true"></v-img>
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

                    <v-text-field class="input-with-icon form_input" name='email' label='E-Mail' v-model='email' type='email' prepend-icon="mail_outline" required></v-text-field>
                    <v-text-field class="input-with-icon form_input" name='name' label='Name' v-model='name' type='text' prepend-icon="face" required></v-text-field>
                    <v-text-field class="input-with-icon form_input" name='password' label='Password' v-model='password' type='password' prepend-icon="lock" required></v-text-field>
                    <v-text-field class="input-with-icon form_input" name='confirmPassword' label='confirmPassword' v-model='confirmPassword' type='password' prepend-icon="check_circle" :rules="[comparePasswords]" required></v-text-field>
                </v-container>
            </v-form>

        </v-row>

        <v-row justify="center" width="200">
                <v-btn round color="#B5D4B8">Back</v-btn>
                <v-spacer></v-spacer>
                <v-btn round color="#B6DCCC">Sign Up</v-btn>

        </v-row>
    </v-container>

</v-card>
</template>

<script>
export default {
    name: 'RegistForm',
    props: {
        source: String,
    },
    data: () => ({
        drawer: null,
    }),
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
