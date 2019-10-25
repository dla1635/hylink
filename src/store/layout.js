export const layout = {
    state: { 
        isNavBarOpen : false
    },
    mutations: {
        changeNavBarState(state){
            state.isNavBarOpen ^= false;
        }
    },
    actions: { 

    },
    getters: {  
        getNavBarState: state => {
            return state.isNavBarOpen;
        }
    }
}