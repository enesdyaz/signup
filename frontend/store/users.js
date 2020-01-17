export const actions = {
    login({ commit }, payload) {
      this.$axios.post('http://localhost:8000/rest-auth/login/', {
        
        username: payload.username,
        password: payload.password,
      }, {
        withCredentials: true,
      })
        .then((res) => {
          alert('login success')

          commit('setMe', res.data);
          this.$router.push('/')
        })
        .catch((err) => {
          console.error(err);
        });
    },
    logout({ commit }) {
      this.$axios.post('http://localhost:8000/rest-auth/logout/', {}, {
        withCredentials: true,
      })
        .then((data) => {
          alert('logout success')
          commit('setMe', null);
          this.$router.push('/')
        })
        .catch((err) => {
          console.error(err);
        });
  
    },

    signup({commit}, payload){
      this.$axios.post('http://localhost:8000/rest-auth/registration/',{
        username: payload.username,
        email: payload.email,
        password1: payload.password1,
        password2: payload.password2,
      }, {withCredentials: true,})
      .then(res => {
        alert('signup success')
        commit('setMe', res.data)
        this.$router.push('/')
      })
      .catch(err => {console.log(err)})

    }
  
};


export const mutations = {
    setMe(state, payload) {
      state.me = payload;
    },
};
  

export const state = () => ({
    me: null,   
  });