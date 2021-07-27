<template>
  <div>
    <div class="album text-muted">
      <h2 style="margin-bottom: 100px;">Последние Тарифы</h2>

      <div class="container">

        <div class="projectCard" v-for="tariff in tariffList" v-bind:key="tariff">
          <router-link v-bind:to="`/Tariff/${tariff.id}`" class="nav-link">
            <div>
              <img class="card-img-top" src="http://s1.iconbird.com/ico/2013/9/452/w512h5121380476717calendar.png" style="height:250px;  object-fit:cover; filter: ">
            </div>
            <div class="card-body">
              <h3 class="card-text" align="center">{{ tariff.title }}</h3>
              <p class="card-text">{{ tariff.subTitle }}</p>
            </div>
          </router-link>
        </div>

      </div>
    </div>



  </div>
</template>

<script>
import axios from "axios";
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  name: "Tariffs",
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
    }
  }
}
</script>
