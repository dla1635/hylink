<template>
    <div id="banner-canvas">
        <v-img src="../../assets/google.jpg" height="500">
            <v-layout
                column
                align-center
                justify-center
                row
                fill-height
                class="white--text"
            >
                <v-flex col-xs-12 class="banner-title">
                    <h1 class="white--text mb-2 display-1 text-xs-center" style="font-weight: 700; opacity: 0.8; text-shadow: 2px 1px #000000">The social network for epic content</h1>
                    <div class="white--text subheading mb-3 text-xs-center" style="font-weight: 700; opacity: 0.8; text-shadow: 2px 1px #000000">Unlesh your creativity without limitations</div>
                    <v-btn
                        class="banner-text"
                        color="#28D190"
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
.banner-canvas{
    margin-bottom: 30px;   
}
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
