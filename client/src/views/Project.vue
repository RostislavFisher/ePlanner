<template>
  <div class="container" style="background-color: #f7f7f7; width: 100%;+-">

    <div class="row d-flex justify-content-center" style="margin-top: 100px; text-align: center; width: 100%; padding-right: 100px; padding-left: 100px;">

      <div class="col-sm-8 blog-main">

        <div class="blog-post">
          <h2 class="blog-post-title">{{ textTitle }}</h2>
          <p class="blog-post-meta"> {{ dateAdded }}</p>
        </div><!-- /.blog-post -->
        <div class="blog-post">
          <span v-html="text"></span>
        </div><!-- /.blog-post -->
        <input-tag placeholder="Введите теги..." v-model="tags" :allow-duplicates="true" :limit="100" :read-only="true"></input-tag>
        <div v-for="item in files" v-bind:key="item">
          <nav class="blog-pagination">
            <a  class="btn btn-outline-primary"
                v-text="'/downloadFile/' + item"  :href="'/downloadFile/' + item" download></a>
          </nav>
        </div>

      </div><!-- /.blog-main -->

    </div>

  </div>
</template>

<script>
import axios from "axios";
import InputTag from "vue-input-tag";
export default {
  name: "project",
  props: ["documentID"],
  components:{
    InputTag
  },
  data(){
    return{
      files: [],
      data: "",
      textTitle: "",
      subTitle: "",
      dateAdded: "",
      text: "",
      tags: [],

    }
  },
  mounted() {
    axios
        .get('/checkIfLogged')
        .then(response => {
          console.log(response.data["userStatus"] === "isLoggined");
          if(response.data["userStatus"] !=="isNotLoggined"){
            axios.get("/checkIfHasItExpired", response => {
              if(response.data["currentlyWorks"]){
                this.getDocumentInfo();
              }
              else{
                console.log("Has been expired");
              }
            })


          }
          else{
            window.location.href = "/";
          }
        });

  },
  methods: {
    getDocumentInfo () {
      console.log(this.$route.params.documentID);
      axios.post(`getInformationOfDocumentByID/${this.documentID}/`, {}).then((response)=>{
        this.data = response.data["data"];
        this.textTitle = this.data["textTitle"];
        this.subTitle = this.data["subTitle"];
        this.dateAdded = this.data["dateAdded"];
        this.text = this.data["text"];
        this.files = this.data["files"];
        this.tags = this.data["tags"];
      });
    }
  }
}
</script>

<style scoped>

</style>