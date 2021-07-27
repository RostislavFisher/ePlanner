<template>
<div>tariffID:{{ tariffID }}</div>
</template>

<script>
import axios from "axios";

export default {
  name: "Tariff",
  props: ["tariffID"],
  data(){
    return{
      time: 0,
      subTitle: ""
    }
  },
  methods: {
    getTariffsList () {
      console.log(this.$route.params.documentID);
      axios.post(`getTargetInformationTariff/${this.tariffID}/`, {}).then((response)=>{
        this.data = response.data["data"];

      });
    }
    },
  mounted(){
    this.getTariffsList();
  }
}
</script>

<style scoped>

</style>