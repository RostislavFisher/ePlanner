<template>
  <div>
    <div>
      <router-link to="/AdminPanel/AdminPanelCreatingDocumentPage/" role="button" class="btn btn-secondary float-sm-left" style="margin-left: 30%;">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
          <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
        </svg>
      </router-link>
      <div class="float-sm-right" style="max-width: 500px; width: 60%; margin-bottom: 50px;">
        <form @submit.prevent="findDocumentByName">
          <input class="form-control mr-sm-2" type="text" placeholder="Пошук" aria-label="Пошук" name="search" id="search" v-model="search">
          <button class="btn btn-primary">Шукати</button>
        </form>
      </div>
    </div>
    <div class="container">

      <div class="projectCard" v-for='documentCard in listOfDocuments' v-bind:key="documentCard">
        <router-link class="nav-link" :to="{ path: `/project/${documentCard.id}`}">
          <div>
            {{ documentCard.id }}
            <img class="card-img-top" src="http://s1.iconbird.com/ico/2013/9/452/w512h5121380476717calendar.png" style="height:250px;  object-fit:cover; filter: ">
          </div>
          <div class="card-body">
            <h3 class="card-text" align="center">{{ documentCard.textTitle }}</h3>
            <p class="card-text">{{ documentCard.subTitle }}</p>

          </div>
        </router-link>
          <div class="dropup float-right">
            <button class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots" viewBox="0 0 16 16">
                <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/>
              </svg>

            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
              <a class="dropdown-item" href="#">Змінити</a>
              <button class="dropdown-item" v-on:click="deleteDocument(documentCard.id)">Видалити</button>
            </div>
          </div>

      </div>

    </div>
  </div>


</template>

<script>
import axios from "axios";

export default {

  name: "AdminDocumentsPage",
  data() {
    return {
      listOfDocuments: null,
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
        this.listOfDocuments = response.data["data"];
      });

    },
    deleteDocument(id){
      axios.post('deleteDocument', {
        params: {
          id : id
        }
      }).then((response) =>{
        console.log(response);
        this.getListOfDocuments();
      });
    },
    findDocumentByName () {
      axios.post('search', {
        params: {
          search: this.search,
        }}).then((response) => {
        this.listOfDocuments = response.data["data"];
      });
    }
  }
}
</script>

<style scoped>

</style>