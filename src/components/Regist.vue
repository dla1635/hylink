<template>
<v-card class="elevation-12" max-width="450">
    <v-toolbar dark flat>
        <v-toolbar-title>Regist</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon dark>
            <v-icon>close</v-icon>
        </v-btn>

    </v-toolbar>

    <v-card-text class="pb-0">
        <v-form>
            <v-container grid-list-md text-xs-center>

                <v-layout wrap row>
                    <v-text-field class="input-with-icon" name='email' label='E-Mail' v-model='email' type='email' prepend-icon="mail_outline" required></v-text-field>
                    <v-text-field class="input-with-icon" name='name' label='Name' v-model='name' type='text' prepend-icon="face" required></v-text-field>
                    <v-text-field class="input-with-icon" name='password' label='Password' v-model='password' type='password' prepend-icon="lock" required></v-text-field>
                    <v-text-field class="input-with-icon" name='confirmPassword' label='confirmPassword' v-model='confirmPassword' type='password' prepend-icon="check_circle" :rules="[comparePasswords]" required></v-text-field>
                </v-layout>
            </v-container>
        </v-form>

    </v-card-text>
    <v-card-actions>
        <v-btn round color="primary" >Sign Up</v-btn>
        <v-btn round color="secondary">Back</v-btn>
    </v-card-actions>
</v-card>
</template>

<script>
export default {
    props: {
        source: String,
    },
    data: () => ({
        drawer: null,
    }),
}
</script>
