<template>
    <div id="welcome-page">
    <!-- 상단 바 -->
        <AppBar />

        <Banner />
    </div>
</template>

<script>
import AppBar from './AppBar'
import Banner from './Banner'

export default {
    name: 'LandingPage',
    components: {
        AppBar,
        Banner,
    },
    data() {
        return {
        }
    },

};
</script>

<style scoped>
#banner-page{
    padding: 0px;
    margin: 0px;
}
</style>
