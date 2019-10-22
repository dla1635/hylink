<template>
<v-card class="elevation-12" max-width="450">
    <v-toolbar dark flat>
        <v-toolbar-title>Login</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon dark>
            <v-icon>close</v-icon>
        </v-btn>
    
    </v-toolbar>
    
    <v-card-text class = "pb-0">
        <v-form>
            <v-text-field label="Login" name="login" prepend-icon="person" type="text"></v-text-field>

            <v-text-field id="password" label="Password" name="password" prepend-icon="lock" type="password"></v-text-field>
            <p class="caption ma-0">Forgot password?</p>
        </v-form>
    </v-card-text>
    <v-card-actions>

        <v-spacer></v-spacer>
        <v-btn>Login</v-btn>
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
