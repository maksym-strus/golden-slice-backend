<script>
import { Line } from 'vue-chartjs';
import chartjsPluginAnnotation from 'chartjs-plugin-annotation'

export default {
  name: 'LineChart',
  extends: Line,
  props: ['chartdata', 'options'],
  mounted () {
    this.addPlugin([chartjsPluginAnnotation]);
    this.renderChart(this.chartdata, this.options)
  }
}
</script>
