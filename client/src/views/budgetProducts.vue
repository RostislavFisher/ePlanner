<template>
  <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4" style="margin-top: 50px;">
    <div class="text-muted">
      <h2 style="margin-bottom: 100px;">Последние Товары</h2>
      <div>
        <div style="width: 33%;">
          <my-chart v-bind:TypeList="this.chartKeys" v-bind:LimitList="this.chartValue"></my-chart>
          <my-chartBarchart v-bind:TypeList="['current', 'roof']" v-bind:LimitList="[this.current, this.roof]"></my-chartBarchart>
        </div>
      </div>
      <div class="float-sm-right" style="max-width: 500px; width: 60%; margin-bottom: 50px;">
          <router-link aria-current="page" href="#" to="/budget/budgetCreateProduct/">
            <button type="button" class="btn btn-secondary">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"></path>
              </svg>
            </button>

          </router-link>

        <form @submit.prevent="findDocumentByName">
          <input class="form-control mr-sm-2" type="text" placeholder="Пошук" aria-label="Пошук" name="search" id="search" v-model="search">
          <button class="btn btn-primary">Шукати</button>
        </form>

      </div>
      <div class="container">

        <div class="projectCard" v-for='product in listOfProducts' v-bind:key="product">
          <router-link class="nav-link" :to="{ path: `/project/${product.id}`}">
            <div>
              <img class="card-img-top" v-bind:src="product.images[0]" style="height:250px;  object-fit:cover; filter: ">
            </div>
            <div class="card-body">
              <h3 class="card-text" align="center">{{ product.text }}</h3>
              <p class="card-text">{{ product.textTitle }}</p>
              <p class="card-text" style="margin-top: 15px;">{{ product.price }}</p>
              <p class="card-text" style="margin-top: 15px;">{{ product.tags[0] }}</p>

            </div>
          </router-link>
        </div>

      </div>
    </div>



  </main>
</template>
<script>
import axios from "axios";
import MyChart from "./myChart";
import myChartBarchartValue from "./myChartBarchartValue";
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';
export default {
  name: "budgetProducts",
  data() {
    return {
      listOfProducts: null,
      search: '',
      chartKeys: [],
      chartValue: [],
      roof: 0,
      current: 0
    }
  },
  mounted() {
    this.getListOfDocuments();
    this.getDataforChart();
  },
  methods: {
    getDataforChart(){
      axios.post('getProductsInfo').then((response) => {
        this.chartKeys = response.data["keys"];
        this.chartValue = response.data["values"];

        this.roof = response.data["budget"]["roof"];
        this.current = response.data["budget"]["current"];
      });
    },
    getListOfDocuments(){
      axios.post('getListOfProducts', {
        params: {
          amountOfDocuments : 5
        }
      }).then((response) => {
        this.listOfProducts = response.data["data"];
      });

    },
    findDocumentByName () {
      axios.post('search', {
        params: {
          search: this.search,
        }}).then((response) => {
        this.listOfProducts = response.data["data"];
      });
    }
  },
  components: {
    'my-chart': MyChart,
    'my-chartBarchart': myChartBarchartValue,
  },
}
</script>

<style scoped>

</style>