
<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
  props: ["TypeList", "LimitList"],
  watch: {
    TypeList: function () {
      this.renderChart({
        labels:  this.TypeList,
        datasets: [
          {
            label: "price",
            data: this.LimitList
          }
        ]
      });
    }
  },
  mounted() {
    this.renderChart({
      labels:  this.TypeList,
      datasets: [
        {
          label: "GitHub Commits",
          data: this.LimitList
        }
      ]
    });
  }
};
</script>
