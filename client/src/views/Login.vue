<template>
  <div style="background-color: #f7f7f7; padding: 100px;">
  <div class="register-form" style="width: 100%; max-width: 420px; padding: 15px; margin: 0 auto; ">
    <form @submit.prevent="loginUser">
      <div class="form-label-group">
        <label for="ur">username</label>
        <input type="text" name="ur" id="ur" v-model="username" class="form-control" placeholder="username" required="" autofocus="">
      </div>
      <div class="form-label-group">
        <label for="pwr">password</label>
        <input type="text" name="pwr" id="pwr" v-model="password" class="form-control" placeholder="password" required="" autofocus="">
      </div>
      <button type="submit" class="btn btn-lg btn-primary btn-block" style="margin-top: 30px;">Login</button>
    </form>
  </div>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

import Vue from 'vue'
export default {
  name: 'Login',
  data () {
    return {
      name: '',
      email: '',
      username: '',
      password: '',
      confirm: ''
    }
  },
  methods: {
    loginUser () {
      axios.post('loginUser', {
        params: {
          username: this.username,
          password: this.password,
        }}).then(response => {
            this.userStatus = response.data["userStatus"];
            if(this.userStatus !== "isNotLogged") {
              window.location.href = "/";

            }
            else{
              console.log("123");
              Vue.notify({
                group: 'foo',
                title: 'Important message',
                text: 'Hello user! This is a notification!'
              })
              }
        }).catch(error => {
        console.log(error) //do some stuff here
      });
    }
  }
}

</script>

<style scoped>

</style>