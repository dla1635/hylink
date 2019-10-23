<template>
<v-container fill-height>
    <v-row justify="center">

        <Regist></Regist>
    </v-row>

</v-container>
</template>

<script>
import Regist from "@/components/Regist"

export default {
    data: () => ({
        drawer: null,
        id: "",
        password: ""
    }),
    components: {
        Regist
    },
    method: {

    }
}
</script>
