export const layout = {
    state: { 
        isNavBarOpen : false
    },
    mutations: {
        changeNavBarState(state){
            state.isNavBarOpen ^= true;
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