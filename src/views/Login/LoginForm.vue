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
                    <v-text-field class="form_input" background-color="#C8EBCC" label="Email" id="email" name="email" prepend-icon="person" type="text" outlined="true" rounded="true" persistent-hint="false" single-line="true" loading="false" dense = "true"></v-text-field>
                    <v-text-field class="form_input" background-color="#C8EBCC" label="Password" id="password" name="password" prepend-icon="lock" type="password" outlined="true" rounded="true" persistent-hint="false" single-line="true" loading="false" dense = "true"></v-text-field>
                    <p class="caption ma-0">Forgot password?</p>
                </v-form>
            </v-row>
            

        </v-container>
    </v-card-text>

    <v-card-actions>
        <v-container>
            <v-row justify="center">
                <v-btn color="#B6DCCC" rounded="true" width="100" height="25">Login</v-btn>
            </v-row>

        </v-container>
    </v-card-actions>
</v-card>
</template>

<script>
export default {
    data: () => ({
        drawer: null,
        id: "",
        password: ""
    }),
    method: {
        async signUp() {
            // 로그인 프로세스

        },
    }
}
</script>

<style scoped>
.form_input {
    width: 300px;
}
