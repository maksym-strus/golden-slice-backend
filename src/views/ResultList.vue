<template>
  <v-container>
    <loading v-if="loading" />
    <v-row v-else>
      <v-col cols="12">
        <h1>Result list</h1>
      </v-col>
      <v-col cols="12" v-for="graphic in graphics" :key="graphic.id">
        <v-card height="180" class="pa-3" @click="getResult(graphic.id)">
          <v-row>
            <v-col cols="2">
              <v-img src="../assets/img/line-graph.png"/>
            </v-col>
            <v-col cols>
              <h2>Formula: {{ graphic.formula }}</h2>
              <h3>Start point: {{ graphic.start_point }}</h3>
              <h3>Step: {{ graphic.step }}</h3>
              <h3>Number of points: {{ graphic.number_of_points }}</h3>
              <h3>Accuracy: {{ graphic.accuracy }}</h3>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import server from "@/utils/server-api";
import Loading from 'vue-loading-overlay';

export default {
  name: "ResultList",
  components: {
    Loading
  },
  data: () => ({
    graphics: [],
    loading: true,
  }),
  mounted() {
    server.get('/graphic')
    .then((res) => {
      this.graphics = res.data
    })
    .finally(() => {
      this.loading = false;
    })
  },
  methods: {
    getResult(id) {
      this.$router.push(`/result/${id}`)
    }
  }
}
</script>
