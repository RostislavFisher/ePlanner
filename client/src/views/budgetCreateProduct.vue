<template>
  <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4" style="margin-top: 50px;">
    <div class="text-muted">
      <h2 style="margin-bottom: 100px;">Добавление товара</h2>
      <form @submit="submit" ref="formHTML" >

      <div class="container">
        <div class="projectCard">
            <div>
              <input type="file" name="file" id="file" ref="file" @change="onFileChange" />
              <img class="card-img-top" v-if="url" :src="url" style="height:250px;  object-fit:cover; filter: ">
            </div>
            <div class="card-body">
              <h3 class="card-text" align="center">
                <input type="text" class="form-control" placeholder="Название товара" aria-label="Название товара" aria-describedby="basic-addon2" ref="budget" style="margin-bottom: 50px;" id="Title" v-model="Title">
              </h3>
              <h3 class="card-text" align="center">
                <input type="text" class="form-control" placeholder="Описание" aria-label="Описание" aria-describedby="basic-addon2" ref="Text" style="margin-bottom: 50px;" id="Text" v-model="Text">
              </h3>
              <h3 class="card-text" align="center">
                <input type="text" class="form-control" placeholder="Цена" aria-label="Цена" aria-describedby="basic-addon2" ref="budget" id="Price" v-model="Price">
              </h3>
            </div>
            <div>
              <div>
                <select id="classification" class="form-control" v-model="tags" >
                    <option v-for="budgetItem in budgetItems" v-bind:key="budgetItem" :value="budgetItem['title']">{{ budgetItem['title'] }}</option>
                </select>
              </div>
              <div>
                <select id="" class="form-control" v-model="family">
                  <option selected value="">
                    Не привязывать к семье
                  </option>
                    <option v-for="family in this.families" v-bind:key="family" :value="family.id">{{ family.title }}</option>
                </select>
              </div>
            </div>
        </div>

      </div>
        <button type="submit" class="btn btn-lg btn-primary btn-block" style="margin-top: 30px;">Создать документ</button>

      </form>

    </div>



  </main>
</template>
<script>
import axios from "axios";
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';
export default {
  name: "budgetCreateProduct",
  data(){
    return{
      url: null,
      tags: "",
      Price: "",
      Title: "",
      text: "",
      tagList: [],
      families: {},
      budgetItems: [],
      family: ""
    }
  },
  mounted() {
    this.getUserData();
  },
  methods: {
      getUserData(){
        axios.post('returnUserInformation').then(result =>
        {
            this.families = result.data["families"];
            this.budgetItems = result.data["budgetItems"];
            console.log(this.families);
            console.log(this.budgetItems);
        });
      },
      onFileChange(e) {
        const file = e.target.files[0];
        this.url = URL.createObjectURL(file);

        let fileForm = new FormData();
        fileForm.append('file', file, file.name)
        this.fileForm = fileForm;

      },
    submit: async function (e) {
      e.preventDefault();

      /* formData */
      var formData = new FormData( this.$refs.formHTML );
      formData.append("clasification", this.tags);
      formData.append("Price", this.Price);
      formData.append("Text", this.Text);
      formData.append("Title", this.Title);
      formData.append("tags", this.tags);
      formData.append("family", this.family);
      /* AJAX request */
      await axios({
        method: "post",
        url: "createDocument",

        data: formData,

        config: { headers: { "Content-Type": "multipart/form-data" } }
      })

          /* handle success */
          .then( response => { console.log(response.data); } )

          /* handle error */
          .catch( response => { console.log(response) } );},

  }
}
</script>

<style scoped>

</style>