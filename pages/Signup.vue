<template>
<div align='center' style='margin-top: 30px;'>
  <v-container>
    <v-card style='width: 350px;height: 420px;' dark>
        <v-card-title class='justify-center'>SIGNUP FORM</v-card-title>
        <v-card-subtitle>
            <v-text-field v-model='username' placeholder="Username"></v-text-field>
            <v-text-field v-model='email' placeholder="email"></v-text-field>
            <v-text-field v-model='password1' placeholder="Password1"></v-text-field>
            <v-text-field v-model='password2' placeholder="Password2"></v-text-field>
        </v-card-subtitle>
        <v-card-action>
            <div class='my-2'>
            <v-btn color='primary'>LOGIN</v-btn>
            </div>
        </v-card-action>
    
    </v-card>      
  </v-container>
</div>
</template>

<script>
export default {

}
</script>

<style>

</style>