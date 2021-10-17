<template>
  <v-container>
    <loading v-if="loading" />
    <v-row v-else>
      <v-col cols="12">
        <h1>Result</h1>
      </v-col>
      <template v-if="resultData.iterations">
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
        <v-col cols="12">
          <p>
            <span v-if="currentIteration !== 0">
              Since
              <vue-mathjax :formula="`$y_{${ currentIteration - 1 }} = ${ currentIterationData.y_value }$`" />,
              <vue-mathjax :formula="`$z_{${ currentIteration - 1 }} = ${ currentIterationData.z_value }$`" />
               and
              <vue-mathjax :formula="`$f(y_{${ currentIteration - 1 }}) = ${ currentIterationData.f_y_value }$`" />,
              <vue-mathjax :formula="`$f(z_{${ currentIteration - 1 }}) = ${ currentIterationData.f_z_value }$`" />
               so
            <vue-mathjax v-if="currentIterationData.is_left_slice" :formula="`$f(y_{${currentIteration - 1}}) < f(z_{${currentIteration - 1}})$`"/>
            <vue-mathjax v-if="currentIterationData.is_right_slice" :formula="`$f(y_{${currentIteration - 1}}) > f(z_{${currentIteration - 1}})$`"/><br>
              then
            </span>
            <vue-mathjax :formula="`$a_{${ currentIteration }} = ${ currentIterationData.start_point_value }$`" />,
            <vue-mathjax :formula="`$b_{${ currentIteration }} = ${ currentIterationData.end_point_value }$`" />
          </p>
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
      </template>
      <template v-else>
        <v-col cols="12">
          <h3 class="d-inline-block">Formula:
            <vue-mathjax :formula="resultData.formula" :safe="false"></vue-mathjax>
          </h3>
          <h3>Result: {{ resultData.result }}</h3>
          <h3>Eps: {{ resultData.acc}}</h3>
        </v-col>
      </template>
    </v-row>
  </v-container>
</template>

<script>
import server from "@/utils/server-api";

import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
import LineChart from "@/views/LineChart";
import { VueMathjax } from 'vue-mathjax'

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
          console.log(err.response.data);
          console.log(err.response);
          this.$router.push({name: 'Home'})
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
    },
    currentIterationData () {
      return this.resultData.iterations[this.currentIteration];
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
