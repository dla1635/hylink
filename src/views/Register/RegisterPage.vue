<template>
<v-container fill-height>
    <v-row justify="center">

        <Register></Register>
    </v-row>

</v-container>
</template>

<script>
import Register from "./RegisterForm"

export default {
    name: 'RegisterPage',
    data: () => ({
        drawer: null,
        id: "",
        password: ""
    }),
    components: {
        Register
    },
    method: {

    }
}
</script>
