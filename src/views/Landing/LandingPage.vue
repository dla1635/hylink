<template>
    <div id="welcome-page">
    <!-- 상단 바 -->
        <AppBar />

        <Banner />

        <Team />
       
    </div>
</template>

<script>
import AppBar from './AppBar'
import Banner from './Banner'
import Team from './Team'

export default {
    name: 'LandingPage',
    components: {
        AppBar,
        Banner,
        Team,
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
