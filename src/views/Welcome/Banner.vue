<template>
    <div id="banner-canvas">
        <v-content>
        <section>
            <v-parallax src="../../assets/cover.jpg" height="500">
            <v-layout
                column
                align-center
                justify-center
                row
                fill-height
                class="white--text"
            >
                <v-flex class="banner-title">
                    <div class="white--text mb-2 display-1 text-center">Share Your Links</div>
                    <v-btn
                        class="banner-text"
                        color="#009CEE"
                        large
                        dark
                        :to="{ name: 'home' }"
                    >
                        Get Started
                    </v-btn>
                </v-flex>
            </v-layout>
            </v-parallax>
      </section>
      </v-content>
    </div>
</template>

<script>
export default {
    name: 'Banner',
    methods: {
        
    },
    created() {
    }
}
</script>

<style scoped>
#banner-canvas{
    margin-top: -10vh;
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
