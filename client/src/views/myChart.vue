
<script>
import { Doughnut } from "vue-chartjs";

export default {
  extends: Doughnut,
  props: ["TypeList", "LimitList"],
  watch: {
    TypeList: function () {
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
    console.log(this.TypeList);
    console.log(this.LimitList);
  }
};
</script>
