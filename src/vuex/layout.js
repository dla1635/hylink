/* eslint-disable */
import Axios from "axios";
import session from '../api/session';

export const layout = {
    state: { 
        isNavBarOpen : false,
        labels:[
            // {name:'Algorithm'},{name:'BigData'},{name:'BlockChain'},{name:'AI'}
        ],
        card_list: [
            {
              title: "알고리즘 분석1알고리즘 분석1알고리즘 분석1알고리즘 분석1",
              summary:"책상이나 바닥처럼 평평한 곳 어디에서든 무선으로 전자기기를 충전할 수 있는 기술이 나왔다.기존의 무선 충전 기술은 공기를 이용해 전력을 주고받는 자기장 신호를 전달해 충전한다.연구팀은 실험과 시뮬레이션을 통해 실제로 이 무선충전 시스템이 기존 방식보다 훨씬 효율적으로 충전할 수 있음을 확인했다.책상이나 바닥처럼 평평한 곳 어디에서든 무선으로 전자기기를 충전할 수 있는 기술이 나왔다.기존의 무선 충전 기술은 공기를 이용해 전력을 주고받는 자기장 신호를 전달해 충전한다.연구팀은 실험과 시뮬레이션을 통해 실제로 이 무선충전 시스템이 기존 방식보다 훨씬 효율적으로 충전할 수 있음을 확인했다.책상이나 바닥처럼 평평한 곳 어디에서든 무선으로 전자기기를 충전할 수 있는 기술이 나왔다.기존의 무선 충전 기술은 공기를 이용해 전력을 주고받는 자기장 신호를 전달해 충전한다.연구팀은 실험과 시뮬레이션을 통해 실제로 이 무선충전 시스템이 기존 방식보다 훨씬 효율적으로 충전할 수 있음을 확인했다.",
              tag: [{name:"알고리즘"},{name:"자바"},{name:"백준"}],
              label: [{name:"Algorithm"},{name:"BigData"}],
              thumbnail: "data:image/png;base64,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",
              url:"http://edu.ssafy.com/edu/main/index.do"
            },
            {
              title: "빅데이터",
              tag: ["빅데이터","자바","깃허브"],
              thumbnail: "https://blogsimages.adobe.com/digitaldialogue/files/2018/10/Digital-Dialogue_Q4-1%ED%9A%8C%EC%B0%A8-%EC%9D%B4%EB%A9%94%EC%9D%BC-%EB%A7%88%EC%BC%80%ED%8C%85-%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%99%80-%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%9C%BC%EB%A1%9C-%EB%82%A0%EA%B0%9C%EB%A5%BC-%EB%8B%AC%EB%8B%A4_03.jpg"
              ,label: ["BlockChain","AI"],
              url:"https://www.naver.com"
            },
          ],
    },
    mutations: {
        changeNavBarState(state){
            state.isNavBarOpen ^= true;
        },
        setCards(state, payload) {
            console.log(payload)
            state.card_list = payload
        },
        setLabels(state, payload) {
            console.log(payload)
            state.labels = payload
        },

    },
    actions: {
        async getLabels({commit}) {
            var resp = await Axios.get("http://localhost:8000/api/label/")
            commit("setLabels", resp.data)
        },
        async getCards({commit}) {
            // console.log("getCard")
            // header = {headers: {'token': payload.token}}
            var resp = await Axios.get("http://localhost:8000/api/linklist/")
            commit("setCards", resp.data)
        },
        async search({commit}, payload) {
            console.log("search", payload)
            var resp = await session.get("http://localhost:8000/api/linklist/",{
                payload ,
              })
            console.log(resp.data)
            commit("setCards", resp.data)
        },
        async postCard({commit}, payload) {            
            var resp = await session.post("http://localhost:8000/api/link/", payload)
            console.log(resp)
        },
        async shareCard({commit}, payload) {            
            var resp = await session.post("http://localhost:8000/api/share/", payload)
            console.log(resp)
            return resp.data.id
        },
        async setCard({commit}, payload) {
            var resp = await session.post("http://localhost:8000/api/link/", payload)
            console.log(resp)
        },
        async deleteCard({commit}, payload) {
            var resp = await session.post("http://localhost:8000/api/link/", payload)
            console.log(resp)
        }
    },
    getters: {  
        getNavBarState: state => {
            return state.isNavBarOpen;
        }
    }
}