<template>
  <v-app>
    <v-main>
      <div class="container">
          <v-row
              align="center"
              justify="center"
              class="mt-6 mb-4"
          >
            <v-col
                cols="6"
            >
              <router-view/>
            </v-col>
          </v-row>
      </div>
          <div class="background-overlay"></div>
    </v-main>
  </v-app>
</template>

<script>
  export default {
  name: "Auth"
  }
</script>

<style scoped>
  .background-overlay {
    background-image: url("../assets/img/auth-background.jpg");
    position: absolute;
    width: 45%;
    height: 100%;
    right: 0;
    top: 0;
    z-index: 1;
  }
  .container {
    z-index: 2;
    position: relative;
  }
</style>
