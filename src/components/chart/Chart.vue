<script>
import { Scatter } from 'vue-chartjs'

import plug from  'chartjs-plugin-annotation';

export default {
  extends: Scatter,
  name: 'Chart',
  props: ['chartdata', 'options','config'],
  mounted() {
    this.addPlugin(plug)

    if (this.config) {
      this.renderChart(this.config.data, this.config.options)
    }
    else {
      this.renderChart(this.chartdata, this.options)
    }
  }
}
</script>