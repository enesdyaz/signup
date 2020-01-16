<template>
<v-app>
<div>
  <v-card
    color="grey lighten-4"
    flat
    
    tile
  >
    <v-toolbar dark>
      <v-toolbar-title> <v-btn nuxt to ='/' >SBM Solution</v-btn> </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn nuxt to ='/login' small color='green'>
        <span>  LOGIN</span>
      </v-btn>

      <v-btn nuxt to='/signup' small >
        <span>SIGNUP</span>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>

    </v-toolbar>
  </v-card>

  <div>
    <nuxt />
  </div>

</div>
</v-app>
</template>

<script>
export default {

}
</script>

<style>

</style>