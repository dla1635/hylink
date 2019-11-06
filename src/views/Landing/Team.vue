<template>
    <v-container d-flex justify-center grid-list-md xs12 row>
        <v-layout my-5 justify-center text-xs-center>
            <span class="display-2 my-5">Team</span>
            <v-flex 
                v-for="profile in profiles"
                :key="profile.name"
                xs12 
                sm12
                text-center
                >
                
                <TeamCard firstName lastName email avatar bio isShelfOpen isEditing />
            </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import TeamCard from './TeamCard'

export default {
    name: 'Team',
    // props: {
    //     firstName: { type:String, default:'' },
    //     lastName: { type:String, default:'' },
    //     email: { type:String, default:'' },
    //     avatar: { type:String, default:'' },
    //     bio: { type:String, default:'Back in my day ... ' },
    //     isShelfOpen: { type:Boolean, default:false },
    //     isEditing: { type:Boolean, default:false },
    // },
    data(){
        return {
            profiles: [
                { name: '서진환', role: 'DB, Frontend', git: 'https://lab.ssafy.com/jinhwan_nim', email: 'nodongth@gmail.com', imgUrl: 'https://lab.ssafy.com/s1-final/hylink/uploads/fd4c61435f6383c914b7a630c884a555/1.PNG'},
                { name: '심창훈', role: 'AI, Chrome-Extension', git: 'https://lab.ssafy.com/', email: 'gilseong223@gmail.com', imgUrl: 'https://lab.ssafy.com/s1-final/hylink/uploads/b87bde7d391b7b9c446df4f73b7b867d/2.PNG'},
                { name: '이동현', role: 'Backend, Server', git: 'https://lab.ssafy.com/', email: 'dicmon@naver.com', imgUrl: 'https://lab.ssafy.com/s1-final/hylink/uploads/631c0de8d994ce6ce73104816141e150/3.PNG'},
                { name: '이하동', role: 'Frontend, Backend', git: 'https://lab.ssafy.com/metleeha', email: 'wsjeongssa1@gmail.com', imgUrl: 'https://lab.ssafy.com/s1-final/hylink/uploads/6571b709cde8f64ea6a972682c61e4b6/4.PNG'},
                { name: '임종완', role: 'Frontend', git: 'https://lab.ssafy.com/', email: 'heabin209@gmail.com', imgUrl: 'https://lab.ssafy.com/s1-final/hylink/uploads/22e2bb3ad6b05fbb774ac6655e497cc5/6.PNG'},
            ],

        }
    },
    components: {
        TeamCard
    }

}
</script>

<style scoped>

</style>