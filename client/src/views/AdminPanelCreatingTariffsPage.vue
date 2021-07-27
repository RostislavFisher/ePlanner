<template>
  <div>
    <form @submit.prevent="createTags"  style="margin-left: 10%; margin-right: 10%; margin-top:50px;">
      <input type="text" placeholder="Введите название..." v-model="title" class="form-control" style="margin-bottom: 20px;">
      <input type="text" placeholder="Введите короткое описание..." v-model="subTitle" class="form-control">
      <input type="number" placeholder="Введите количество дней..." v-model="time" min="1" class="form-control">

      <input type="submit" class="btn btn-lg btn-primary btn-block" style="margin-top: 20px;">
    </form>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  name: "AdminPanelCreatingTariffsPage",
  components:{
  },
  data() {
    return {
      title: "",
      subTitle: "",
      time: 0
    };
  },
  methods:{
    createTags(){
      axios.post('createTariff', {
        params: {
          title: this.title,
          subTitle: this.subTitle,
          time: this.time,
        }});
    }
  }
}

</script>

<style scoped>

</style>