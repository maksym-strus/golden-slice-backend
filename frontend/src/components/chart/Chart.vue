<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  name: 'Chart',
  props: ['chartdata', 'options'],
  mounted() {
    this.renderChart(this.chartdata, this.options)
  }
}
</script>