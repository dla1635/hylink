<template id="member-list">
    <div>
        <div class="loading" v-if="loading">로딩 중 ...</div>
        <div v-if="error" class="error">
            {{ error }}
        </div>
        <!-- members 의 로딩이 끝나면 각 팀원의 이름을 표시 -->
        <div v-for="member in members" :key="member.id">
            <h2>{{ member.name }}</h2>
            <p>{{ member.description }}</p>
        </div>
    </div>
</template>

<script>
var getMembers = function(callback) {
    setTimeout(function(){
            callback(null, [{
                id: 1,
                name: '서진환',
                description: '팀장. DBA, 백엔드(인증), 프론트엔드(랜딩페이지, 로그인)'
            },
            {
                id: 2,
                name: '심창훈',
                description: '크롤링, AI(제목, 세줄 요약, 태그)'
            },
            {
                id: 3,
                name: '이동현',
                description: '백엔드(링크), 서버(AWS)'
            },
            {
                id: 4,
                name: '이하동',
                description: '백엔드(게시판, 회원가입), 프론트엔드(사이드바, 팀소개)'
            },
            {
                id: 5,
                name: '임종완',
                description: '프론트엔드(링크카드, 메인)'
            }
        ])
    }, 1000)
}

export default {
    name: "aboutus",
    data(){
        return {
            loading: false,
            members: function() {
                return []
            },
            error: null
        }
    },
    // 초기화할 때 데이터를 받아옴 
    created: function() {
        this.fetchData()
    },

    // $route의 변경을 모니터링하며 라우팅이 수정되면 데이터를 다시 받아옴 
    watch: {
        '$route': 'fetchData'
    },

    methods: {
        fetchData: function() {
            this.loading = true 
            // Function.prototype.bind는 this의 유효범위를 전달하기 위해 사용 
            getMembers((function(err, members) {
                this.loading = false
                if (err) {
                    this.error = err.toString()
                } else {
                    this.members = members
                }
            }).bind(this))
        }
    }
}
</script>