<template>
  <v-container>
    <Loading v-if="loading" />
    <v-row v-else>
      <v-col cols="12">
        <h1>Result</h1>
      </v-col>

      <v-col cols="12">
        <h3>Result is: {{ resultData.result }}</h3>
        <h3>Point a: {{ resultData.start_point }}</h3>
        <h3>Point b: {{ resultData.end_point }}</h3>
        <h3>Eps: {{ resultData.acc}}</h3>
        <h3>Number of iterations: {{ resultData.number_of_iterations}}</h3>
      </v-col>

      <v-col cols="6" v-for="(chart,key) in resultData.iterations" :key="key">
        <apex-chart type="line" :series="series" :options="prepareData(chart)"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import server from "@/utils/server-api";
import ApexChart from 'vue-apexcharts'

import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';

export default {
name: "Result",
  components: {
    Loading,
    ApexChart
  },
  data: () => ({
    resultData: null,
    loading: true
  }),
  props: ['id'],
  mounted() {
    server
        .get(`/graphic/${this.id}`)
        .then((res) => {
          this.resultData = res.data
        })
        .catch((err) => {
          this.$router.push({name: 'Home'})
          console.log(err.response.data)
        })
      .finally(() => {
        this.loading = false
      })
  },
  computed: {
    points() {
      return this.resultData && this.resultData.x_values.map((x, idx) => ({x, y: this.resultData.y_values[idx]}))
    },
    series() {
      return [{
        name: 'f(x)',
        data: this.points,

      }]
    }
  },
  methods: {
    prepareData(points) {
      return {
        xaxis: {
          labels: {
            show: false
          }
        },
        yaxis: {
          labels: {
            show: false
          }
        },
        chart: {
          id: 'vuechart-example',
        },
        annotations: {
          xaxis: [
            {
              x: points.start_point,
              borderColor: 'red',
            },
            {
              x: points.end_point,
              borderColor: 'red',
            },
          ]
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
