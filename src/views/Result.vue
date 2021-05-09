<template>
  <v-container>
    <loading v-if="loading" />
    <v-row v-else>
      <v-col cols="12">
        <h1>Result</h1>
      </v-col>
      <v-col cols="12">
        <h3 class="d-inline-block">Formula:
          <vue-mathjax :formula="resultData.formula" :safe="false"></vue-mathjax>
        </h3>
        <h3>Result: {{ resultData.result }}</h3>
        <h3>Point a: {{ resultData.start_point }}</h3>
        <h3>Point b: {{ resultData.end_point }}</h3>
        <h3>Eps: {{ resultData.acc}}</h3>
        <h3>Number of iterations: {{ resultData.number_of_iterations}}</h3>
        <h3>Current iteration: {{ currentIteration + 1 }}</h3>
      </v-col>

      <v-col cols="12" v-if="resultData">
        <v-carousel
            v-model="currentIteration"
            hide-delimiters
            :cycle="false"
            height="500"
        >
          <v-carousel-item
              v-for="(chart,key) in resultData.iterations"
              :key="key"
          >
            <line-chart :styles="myStyles" :options="prepareLabel(chart)" :chartdata="chartdata"/>
          </v-carousel-item>
        </v-carousel>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
import server from "@/utils/server-api";

import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
import LineChart from "@/views/LineChart";
import {VueMathjax} from 'vue-mathjax'

export default {
name: "Result",
  components: {
    LineChart,
    Loading,
    'vue-mathjax': VueMathjax
  },
  data: () => ({
    resultData: null,
    loading: true,
    currentIteration: 0,
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
    chartdata() {
      return {
        labels: this.resultData ? this.resultData.x_values : [],
        datasets: [{
          label: 'f(x)',
          data: this.resultData ? this.resultData.y_values : [],
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      }
    },
    myStyles () {
      return {
        height: '500px',
        position: 'relative'
      }
    }
  },
  methods: {
    prepareLabel(points) {
      return {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [{
            ticks: {
              maxTicksLimit: 9,
            }
          }]
        },
        annotation: {
          annotations: [
            {
              id: 'vline-1',
              type: 'line',
              mode: 'vertical',
              scaleID: 'x-axis-0',
              value: points.start_point,
              borderColor: 'red',
              borderWidth: 2,
            },
            {
              id: 'vline-2',
              type: 'line',
              mode: 'vertical',
              scaleID: 'x-axis-0',
              value: points.end_point,
              borderColor: 'red',
              borderWidth: 2,
            }
          ]
        },
      }
    },
  }
}
</script>
