<template>
  <div style="background-color: #f7f7f7; padding: 100px;">
  <div class="register-form" style="width: 100%; max-width: 420px; padding: 15px; margin: 0 auto; ">
    <form @submit.prevent="registerUser">
      <div class="form-label-group">
        <label for="ur">username</label>
        <input type="text" name="ur" id="ur" v-model="username" class="form-control" placeholder="username" required="" autofocus="">
      </div>
      <div class="form-label-group">
        <label for="el">Email</label>
        <input type="text" name="el" id="el" v-model="email" class="form-control" placeholder="Email address" required="" autofocus="">
      </div>
      <div class="form-label-group">
        <label for="pwr">password</label>
        <input type="text" name="pwr" id="pwr" v-model="password" class="form-control" placeholder="password" required="" autofocus="">
      </div>
      <div class="form-label-group">
        <label for="pass">Password Confirmation</label>
        <input type="text" name="pass" id="pass" v-model="confirm" class="form-control" placeholder="password" required="" autofocus="">
      </div>
      <button type="submit" class="btn btn-lg btn-primary btn-block" style="margin-top: 30px;">Register</button>
    </form>
  </div>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

export default {
  name: 'Register',
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
    registerUser () {
      axios.post('registerUser', {
        params: {
          name: this.name,
          email: this.email,
          username: this.username,
          password: this.password,
          confirm: this.confirm
        }}).then(
          window.location.href = "/"
      )
    }
  }
}
</script>
