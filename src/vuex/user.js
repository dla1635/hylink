export const layout = {
    state: { 
        isLogined : true
    },
    mutations: {
        login(state){
            // 세션 로그인 기능 구현
            var a = "0"
            if(a == 0){
                state.isLogined = true;
            }
        },
        logout(state){
            state.isLogined = false;
            // 세션 로그아웃 구현
        }
    },
    actions: { 

    },
    getters: {  
        getLoginState: state => {
            return state.isNavBarOpen;
        }
    }
}