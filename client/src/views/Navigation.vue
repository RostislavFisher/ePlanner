<template>
  <nav class="navbar navbar-expand-sm bg-primary navbar-dark">
    <ul class="navbar-nav" style="  width: 100%;">
      <li class="nav-item active">
        <router-link to="/" class="nav-link">ua_files</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/about/" class="nav-link">Информация</router-link>
      </li>
      <li class="nav-item" v-if="userStatus==='isLoginned'">
        <router-link to="/products/" class="nav-link">Мои товары</router-link>
      </li>
      <li class="nav-item" v-if="userStatus==='isLoginned'">
        <router-link to="/budget/" class="nav-link">Бюджет</router-link>
      </li>
      <li class="nav-item dropdown" v-if="userStatus==='isLoginned'">

        <a class="nav-link dropdown-toggle" href="#" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
            <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
          </svg></a>
        <div class="dropdown-menu" aria-labelledby="dropdown01">
          <router-link to="/Account/" class="dropdown-item">Мой профиль</router-link>
          <button class="dropdown-item" v-on:click="logOut">Выйти</button>
        </div>
      </li>
      <li class="nav-item dropdown" v-else-if="userStatus==='isStaff'">
        <a class="nav-link dropdown-toggle" href="#" id="dropdown02" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
            <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
          </svg></a>
        <div class="dropdown-menu" aria-labelledby="dropdown01">
          <router-link to="/Account/" class="dropdown-item">Мой аккаунт</router-link>
          <router-link to="/AdminPanel/" class="dropdown-item">Админ-панель</router-link>
          <button class="dropdown-item" v-on:click="logOut">Выйти</button>
        </div>
      </li>

      <li class="nav-item dropdown" v-else>
        <a class="nav-link dropdown-toggle" href="#" id="dropdown03" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
            <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
          </svg></a>
        <div class="dropdown-menu" aria-labelledby="dropdown01">
          <router-link to="/Login/" class="dropdown-item">Войти</router-link>
          <router-link to="/Register/" class="dropdown-item">Зарегестрироваться</router-link>
        </div>
      </li>
      <li class="nav-item">
      </li>
    </ul>


  </nav>
</template>

<script>
import axios from "axios";

export default {
  name: "Navigation",
  data() {
    return {
      userStatus: "",
    };
  },
  methods: {
    logOut(){
      axios({
        method: 'post',
        url: 'logOut',
      }).then(
        window.location.href = "/").catch((error) => {
        console.log(error);
      })
    }
  },
  mounted() {
    axios
        .get('/checkIfLogged')
        .then(response => {
          this.userStatus = response.data["userStatus"]

        });
  },
}
</script>

<style scoped>

</style>