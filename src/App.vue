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
     isLoading: true
   }),
   created() {
     server.post('/auth/check', {
       token: localStorage.getItem('accessToken')
     })
     .catch(() => {
       this.$store.dispatch('setAuth', false)
       this.$router.push({name: 'Login'})
     })
     .finally(() => {
       this.isLoading = false
     })
   }
 }
</script>

