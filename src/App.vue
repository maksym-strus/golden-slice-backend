<template>
  <div v-if="!isLoading">
    <router-view/>
  </div>
  <div v-else>
    <loading :active.sync="isLoading" />
  </div>
</template>
<script>
 import Loading from 'vue-loading-overlay';
 import 'vue-loading-overlay/dist/vue-loading.css';

 import server from "./utils/server-api";

 export default {
   name: 'App',
   components: {
     Loading
   },
   data: () => ({
     isLoading: false
   }),
   mounted() {
     this.isLoading = true

     server.post('/auth/check', {
       token: localStorage.getItem('accessToken')
     })
      .then(() => {
        this.$store.dispatch('setAuth', true)

        this.$router.push({ name: 'Main'})
      })
     .catch(() => {
       this.$router.push({name: 'Login'})
     })
     .finally(() => {
       this.isLoading = false
     })
   }
 }
</script>

