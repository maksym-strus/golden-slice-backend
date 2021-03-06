<template>
  <v-app>

    <v-navigation-drawer app>
      <nav-bar/>
    </v-navigation-drawer>

    <v-main class="grey lighten-5" app>

      <v-container fluid>
        <router-view/>
      </v-container>

    </v-main>

  </v-app>
</template>

<script>
import NavBar from "../components/nav-bar/NavBar";
export default {
name: "Main",
  components: {NavBar}
}
</script>

<style scoped>

</style>