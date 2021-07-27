<template>
  <div style="padding: 100px;">
      <div class="register-form" style="width: 100%; max-width: 1000px; padding: 15px; margin: 0 auto; ">
<!--      <form @submit.prevent="createDocument">-->
      <form @submit="submit" ref="formHTML" >
        <div class="form-label-group">
          <label for="Title">Title</label>
          <input type="text" name="Title" id="Title" v-model="textTitle" class="form-control" placeholder="Title" required="" autofocus="">
        </div>
        <div class="form-label-group">
        </div>
        <input type="file" name="file" id="file" ref="file" v-on:change="attachmentCreate($event);">
        <input id="text" v-model="text" type="hidden" name="text">
        <trix-editor input="text" id="trix-text-editor"></trix-editor>
        <input-tag placeholder="Введите теги..." :allow-duplicates="true" :limit="-1" type="tags" id="tags" v-model="tags"></input-tag>
        <button type="submit" class="btn btn-lg btn-primary btn-block" style="margin-top: 30px;">Создать документ</button>
      </form>
    </div>
  </div>
</template>

<script>
import InputTag from 'vue-input-tag';
import axios from "axios";
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  name: "AdminPanelCreatingDocumentPage",
  components: {
    InputTag
  },
  data () {
    return {
      textTitle: '',
      fileForm: null,
      form: {},
      text: "<h1>Текст пишіть сюди</h1>",
      tags:[]
    }
  },
  mounted() {
    window.addEventListener("trix-file-accept", function(event) {
      event.preventDefault();
      alert("Це поле не підтримує прикріплення фотографій");
    })
  },
  methods: {
    attachmentCreate() {
      let fileForm = new FormData();
      let file = event.target.files[0];
      fileForm.append('file', file, file.name)
      this.fileForm = fileForm;
    },
    submit: async function (e) {
      e.preventDefault();

      /* formData */
      var formData = new FormData( this.$refs.formHTML );
      console.log(this.tags);
      formData.append("tags", this.tags);
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

<style>
.trix-button-group--file-tools { display: none !important; }
</style>