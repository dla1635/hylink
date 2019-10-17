import axios from 'axios'
import router from '../router/router'

export const Actions = {
    createTeam({commit}, payload) {
      axios.post('http://localhost:8080/TeamChin/insertTeam', payload).then(response => {
          commit('createTeamSuccess')
          if (response.status === 201) {
              location.reload('/')
              console.log('서버연결?!?!?!')
          }
      })
    },
  getAlarmInfo ({ commit }, token) {
    axios.get('https://weatherook.cf/user/news', {
      headers: {
        'token': token
      }
    }).then(response => {
      commit('getAlarmSuccess', response.data)
    })
  }
}