import Axios from "axios"
import Router from "../router";

export const Actions = {

    signUp(dispatch, loginObj) {
      // login => 토큰 반환 
      Axios.post('http://127.0.0.1:8000/api/users/rest-auth/registration/', loginObj)
        .then(res => {
          this.$swal('회원가입 성공', '환영합니다!', 'OK')
          Router.push({
            name: 'login'
          });
          // eslint-disable-next-line no-console
          console.log(res)
        })
        .catch(() => {
          this.$swal({
            type: 'error',
            title: 'Oops...',
            text: '아이디, 이메일, 비밀번호를 확인해주세요!',
          })
        })
    },

  login(dispatch, loginObj) {
    // login => 토큰 반환 
    Axios.post('http://127.0.0.1:8000/api-auth/login/', loginObj)
    .then(res => {
      // 접근 성공시, 토큰 값이 반환된다. (토큰과 user id를 받아옴)
      // 토큰을 헤더 정보에 포함시켜서 유저 정보를 요청한다. 
      let token = res.data.token;
      // 토큰을 로컬에 저장한다. 
      localStorage.setItem("access_token", token);
      this.dispatch("getMemberInfo");
      Router.push({name: 'home'});
      // eslint-disable-next-line no-console
      console.log(res);
    })
    .catch(()=>{
      alert("이메일과 비밀번호를 입력해주세요.")
    })
  },
  logout({ commit }) {
    commit('logout');
    Router.push({ name: "home" });
  },

  getMemberInfo({commit}) {
    let token = localStorage.getItem("access_token");
    let config = {
      headers: {
        "access_token": token
      }
    };
    // 토큰 => 멤버 정보 반환 
    // 새로고침 => 토큰만 가지고 멤버 정보 반환 가능 
    Axios.get("http://127.0.0.1:8000/api/user/", config)
    .then(res => {
      let userInfo = {
        pk: res.data.data.pk,
        email: res.data.data.email,
        nickname: res.data.data.nickname
      };
      commit("loginSuccess", userInfo);
    })
    .catch(() => {
      alert("이메일과 비밀번호를 확인하세요.")
    })
  }
  //   createTeam({commit}, payload) {
  //     axios.post('http://localhost:8080/TeamChin/insertTeam', payload).then(response => {
  //         commit('')
  //         if (response.status === 201) {
  //             location.reload('/')
  //             console.log('서버연결?!?!?!')
  //         }
  //     })
  //   },
  // getAlarmInfo ({ commit }, token) {
  //   axios.get('', {
      
  //   }).then(response => {
  //     commit('getAlarmSuccess', response.data)
  //   })
  // }
}