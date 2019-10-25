<template>
<v-container fill-height>
    <v-row justify="center">
        <v-img alt="Logo" src="@/assets/link.png" max-width="500" max-height="500" contain></v-img>
        <Login height="500"></Login>
    </v-row>
    
</v-container>

</template>

<script>
import Login from "@/components/login/Login"

export default {
    data: () => ({

    }),
    components: {
        Login
    },
    method : {
        
    }
}
</script>
