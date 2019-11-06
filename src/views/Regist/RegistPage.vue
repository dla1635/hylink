<template>

<v-container fill-height>
    <v-row justify="center">

        <Register></Register>
    </v-row>

</v-container>
</template>

<script>
import Register from "./RegistForm"

export default {
    name: 'RegistPage',
    data: () => ({
        drawer: null,

    }),
    components: {
        Register
    },
    method: {

    }
}
</script>
