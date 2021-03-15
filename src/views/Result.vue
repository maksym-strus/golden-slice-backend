<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h1>Result</h1>
      </v-col>

      <v-col cols="12">
        <h3>Result is: 1.000004</h3>
        <h3>Point a: 1</h3>
        <h3>Point b: 2</h3>
        <h3>Eps: 0.0000001</h3>
        <h3>Number of iterations: 5</h3>
      </v-col>

      <v-col cols="4" v-for="n in 5" :key="n">
        <chart/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Chart from "../components/chart/Chart";
export default {
name: "Result",
  components: {
  Chart
  },
  props: ['id'],

}
</script>

<style scoped>

</style>
