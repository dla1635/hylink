<template>
<v-container fill-height>
    <v-row justify="center">

        <Regist></Regist>
    </v-row>

</v-container>
</template>

<script>
import Regist from "./RegistForm"

export default {
    name: 'RegistPage',
    data: () => ({
        drawer: null,

    }),
    components: {
        Regist
    },
    method: {

    }
}
</script>
