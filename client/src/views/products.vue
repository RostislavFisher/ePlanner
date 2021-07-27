<template>
  <div>
    <div class="album text-muted">
      <h2 style="margin-bottom: 100px;">Последние Товары</h2>
      <div class="float-sm-right" style="max-width: 500px; width: 60%; margin-bottom: 50px;">
        <form @submit.prevent="findDocumentByName">
          <input class="form-control mr-sm-2" type="text" placeholder="Пошук" aria-label="Пошук" name="search" id="search" v-model="search">
          <button class="btn btn-primary">Шукати</button>
        </form>

      </div>
      <div class="container">

        <div class="projectCard" v-for='product in listOfProducts' v-bind:key="product">
          <router-link class="nav-link" :to="{ path: `/project/${product.id}`}">
            <div>
              <img class="card-img-top" src="http://s1.iconbird.com/ico/2013/9/452/w512h5121380476717calendar.png" style="height:250px;  object-fit:cover; filter: ">
            </div>
            <div class="card-body">
              <h3 class="card-text" align="center">{{ product.textTitle }}</h3>
              <p class="card-text">{{ product.subTitle }}</p>

            </div>
          </router-link>
        </div>

      </div>
    </div>



  </div>
</template>

<script>
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

export default {

  name: "documents",
  data() {
    return {
      listOfProducts: null,
      search: '',
    }
  },
  mounted() {
    this.getListOfDocuments();
  },
  methods: {
    getListOfDocuments(){
      axios.post('getListOfDocuments', {
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
  }
}
</script>

<style scoped>

</style>

