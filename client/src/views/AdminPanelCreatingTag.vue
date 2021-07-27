<template>
<div>
  <form @submit.prevent="createTags"  style="margin-left: 10%; margin-right: 10%; margin-top:50px;">
    <input-tag placeholder="Введите теги..." v-model="tags" :allow-duplicates="true" :limit="100"></input-tag>
    <input type="submit" class="btn btn-lg btn-primary btn-block" style="margin-top: 20px;">
  </form>


</div>
</template>

<script>
import InputTag from 'vue-input-tag';
import axios from "axios";
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  name: "AdminPanelCreatingTag",
  components:{
    InputTag
  },
  data() {
    return {
      tags: [],
    };
  },
  methods:{
    createTags(){
      axios.post('createTags', {
        params: {
          tags: this.tags
        }});
    }
  }

}
</script>

<style scoped>

</style>