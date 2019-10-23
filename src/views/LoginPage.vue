<template>
<v-container fill-height>
    <v-row justify="center">
        <v-img alt="Logo" src="@/assets/link.png" max-width="500" max-height="500" contain="true"></v-img>
        <Login height="500"></Login>
    </v-row>
    
</v-container>

</template>

<script>
import Login from "@/components/Login"

export default {
    data: () => ({
        drawer: null,
        id : "",
        password: ""
    }),
    components: {
        Login
    },
    method : {
        async signUp() {
            // 로그인 프로세스

        },
    }
}
</script>
