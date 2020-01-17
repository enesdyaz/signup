<template>
<div>
  <v-container v-if='!me'>
  <div align='center'>
    <v-card style='width:300px;'>
      <v-card-title class='justify-center'> LOGIN </v-card-title>
      <v-card-subtitle>
        <v-text-field v-model='username' placeholder="Username"></v-text-field>
        <v-text-field v-model='password' placeholder="Password"></v-text-field>
        <v-btn color='green' @click='login()' type='submit'>LOGIN</v-btn>
      </v-card-subtitle>
    </v-card>
  </div>
  </v-container>

  <v-container v-else>
    <v-card>
      <v-title> Hello, {{me.user.username}} </v-title>
      <v-btn @click='logout()'>LOGOUT</v-btn>
    </v-card>
  </v-container>


</div>
</template>

<script>
export default {
  name: 'login',
  data(){
    return{
      username: '',
      password: '',
    }
  },

   computed: {
      me() {
        return this.$store.state.users.me;
      }
    },

  methods: {
    login(){
      this.$store.dispatch('users/login', {
      username: this.username,
      password: this.password,  
       })
   },
   logout(){
     this.$store.dispatch('users/logout')
   }

  },
}
</script>

<style>

</style>