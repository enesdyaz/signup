<template>
<div>
  <v-container>
  <div align='center'>
    <v-card style='width:300px;'>
      <v-card-title class='justify-center'> SIGNUP </v-card-title>
      <v-card-subtitle>
        <v-text-field v-model='username' placeholder="Username"></v-text-field>
        <v-text-field v-model='email' placeholder="email"></v-text-field>
        <v-text-field v-model='password1' placeholder="Password1"></v-text-field>
        <v-text-field v-model='password2' placeholder="Password2"></v-text-field>
        <v-btn color='green' @click='signup()' type='submit'>SIGNUP</v-btn>
      </v-card-subtitle>
    </v-card>
  </div>
  </v-container>

</div>
</template>

<script>
export default {
  name: 'login',
  data(){
    return{
      username: '',
      email: '',
      password1: '',
      password2: '',
    }
  },

  methods: {
    signup(){
      this.$store.dispatch('users/signup', {
      username: this.username,
      email: this.email,
      password1: this.password1,  
      password2: this.password2,  
       })
     },
  },
};
</script>

<style>

</style>