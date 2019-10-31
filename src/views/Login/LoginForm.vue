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
                    <v-text-field   class="form_input" 
                                    background-color="#C8EBCC" 
                                    label="Email" 
                                    v-model="email" 
                                    id="email" 
                                    name="email" 
                                    prepend-icon="person" 
                                    type="text" 
                                    outlined="true" 
                                    rounded="true" 
                                    single-line="true" 
                                    loading="false" 
                                    dense="true"
                                    v-validate="'required|email'"
                                    data-vv-as="Email"
                                    >
                    </v-text-field>
                    <v-text-field class="form_input" background-color="#C8EBCC" label="Password" v-model="password" id="password" name="password" prepend-icon="lock" type="password" outlined="true" rounded="true" persistent-hint="false" single-line="true" loading="false" dense="true"></v-text-field>
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
    name: 'LoginForm',
    data: () => ({
        email: "",
        password: "",
        rules: {
            required: value => !!value || 'Required.',
            email: value => {
                const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                return pattern.test(value) || 'Invalid e-mail.'
            }
        }
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
