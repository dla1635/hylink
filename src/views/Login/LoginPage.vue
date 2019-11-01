<template>
<v-container fill-height>
    <v-row justify="center">
        <v-img alt="Logo" src="@/assets/link.png" max-width="500" max-height="500" contain="true"></v-img>
        <Login height="500"></Login>
    </v-row>
    
</v-container>

</template>

<script>
import Login from "./LoginForm"

export default {
    name: 'LoginPage',
    data: () => ({
        drawer: null,
        id : "",
        password: ""
    }),
    components: {
        Login
    },
    method : {
        
    }
}
</script>
