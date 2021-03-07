<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h1>Result list</h1>
      </v-col>
      <v-col cols="12" v-for="i in 10" :key="i**2">
        <v-card height="180" class="pa-3">
          <v-row>
            <v-col cols="2">
              <v-img src="../assets/img/line-graph.png"/>
            </v-col>
            <v-col cols>
              <h2>Work: {{i}}</h2>
              <h4>Point a: 1</h4>
              <h4>Point b: 2</h4>
              <h4>Eps: 0.0001</h4>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
name: "ResultList"
}
</script>

<style scoped>

</style>