<template>
<Regist></Regist>
</template>

<script>
import Regist from "@/components/Regist"

export default {
    data: () => ({
        drawer: null,
        id : "",
        password: ""
    }),
    components: {
        Regist
    },
    method : {
        async signUp() {
            // 로그인 프로세스

        },
    }
}
</script>
