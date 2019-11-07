<template>
    <div id="welcome-page">
        <AppBar />

        <Banner />

        <Service />

        <ContactUs />
        
        <Footer />

    </div>
</template>

<script>
import AppBar from './AppBar'
import Banner from './Banner'
import Service from './Service'
import ContactUs from './ContactUs'
import Footer from './Footer'

export default {
    name: 'LandingPage',
    components: {
        AppBar,
        Banner,
        Service,
        ContactUs,
        Footer
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
