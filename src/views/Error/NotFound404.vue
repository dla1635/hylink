<template>
<v-container>
    <!-- 상단 바 -->
    <AppBar></AppBar>
    404 ERROR!
</v-container>
</template>

<script>
import AppBar from './AppBar'

export default {
    name: "404",
    components: {
        AppBar,
    },
    data() {
        return {
        }
    }
};
</script>

<style scoped>
#container {
    background-color: white;
}
</style>
