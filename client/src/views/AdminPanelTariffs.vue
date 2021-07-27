<template>
  <div>
    <div style="margin-bottom: 100px;">
      <router-link to="/AdminPanel/AdminPanelCreatingTariffsPage/" role="button" class="btn btn-secondary float-sm-left" style="margin-left: 30%;">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
          <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
        </svg>
      </router-link>
    </div>

    <div class="table-responsive">
      <table class="table table-striped table-sm">
        <thead>
        <tr>
          <th>#</th>
          <th>Название</th>
          <th>Количество дней подписки</th>
          <th>Функции</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="tariff in tariffList" v-bind:key="tariff">
          <td>{{ tariff.id }}</td>
          <td>{{ tariff.title }}</td>
          <td>{{ tariff.time }}</td>
          <td data-v-5caa450d="">
            <div class="dropdown float-right">
              <button class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots" viewBox="0 0 16 16">
                  <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/>
                </svg>

              </button>
              <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item" href="#">Змінити</a>
                <button class="dropdown-item" v-on:click="deleteTariff(tariff.id)">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                    <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                  </svg>
                  Видалити</button>
              </div>
            </div></td>
        </tr>

        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  name: "AdminPanelTariffs",
  data(){
    return{
      tariffList: []
    }

  },
  mounted(){
    this.getTariffs();
  },
  methods:{
    getTariffs(){
      axios.get("/getTariffsList").then(response=>{
        this.tariffList = response.data["tariffs"]
        console.log(this.tariffList);
      });
    },
    deleteTariff(tariffID){
      axios.delete(`/deleteTariff/${tariffID}/`).then(
        this.getTariffs())
    },
  }
}
</script>

<style scoped>

</style>