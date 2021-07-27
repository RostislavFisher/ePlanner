<template>
  <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4" style="margin-top: 50px;">
    <div class="text-muted">
      <h2 style="margin-bottom: 100px;">Создание семьи</h2>
      <form @submit="submit" ref="formHTML" >

        <div class="container">
          <div class="projectCard">
            <div class="card-body">
              <h3 class="card-text" align="center">
                <input type="text" class="form-control" placeholder="Название семьи" aria-label="Название семьи" aria-describedby="basic-addon2" ref="budget" id="Title" v-model="Title">
              </h3>
            </div>
          </div>

        </div>
        <button type="submit" class="btn btn-lg btn-primary btn-block" style="margin-top: 30px;">Создать семью</button>

      </form>

    </div>
  </main>
</template>
<script>
import axios from "axios";
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';
export default {
  name: "createFamily",
  data(){
    return{
      Title: ""
    }
  },
  methods: {
    submit: async function (e) {
      e.preventDefault();
      axios.get('createFamily', {
        params: {
          Title: this.Title
        }})
          /* handle success */
          .then( response => { console.log(response.data); } )

          /* handle error */
          .catch( response => { console.log(response) } );},

  }
}
</script>

<style scoped>

</style>