<template>
  <v-app>
    <v-main>
      <v-parallax
          height="900"
          src="../assets/img/auth-background.jpg"
      >
        <v-row
            align="center"
            justify="center"
        >
          <v-col
              cols="4"
          >
            <router-view/>
          </v-col>
        </v-row>
        <div class="background-overlay"></div>
      </v-parallax>
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
    background-color: #fafafa;
    position: absolute;
    width: 60%;
    height: 100%;
    right: 0;
    z-index: -1;
  }
</style>