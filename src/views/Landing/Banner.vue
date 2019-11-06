<template>
    <div id="banner-canvas">
            <v-img src="../../assets/cover.jpg" height="500">
                <v-layout
                    column
                    align-center
                    justify-center
                    row
                    fill-height
                    class="white--text"
                >
                    <v-flex col-xs-12 class="banner-title">
                        <div class="white--text mb-2 display-1 text-center">Share Your Links</div>
                        <v-btn
                            class="banner-text"
                            color="#009CEE"
                            large
                            dark
                            @click='toHome'
                        >
                            Get Started
                        </v-btn>
                    </v-flex>
                </v-layout>
            </v-img>
    </div>
</template>

<script>
import router from '../../config/router'

export default {
    name: 'Banner',
    methods: {
        toHome: () => {
            router.push('/home/label/total')
        }
    },
    created() {
    }
}
</script>

<style scoped>
/* #banner-canvas{
    margin-top: -10vh;
} */
.banner-title{
    padding-top: 25vh;
    text-align: center;
    /* line-height:1.2em;  */
    color:#f2f2f2; 
    font-size:2em; 
    font-family: Ubuntu;
}
.banner-text{
    margin: 2rem 2rem;
}
</style>
