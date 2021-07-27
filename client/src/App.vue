<template>
  <div id="app" class="app">
    <Navigation></Navigation>
    <transition name="moveInUp">
    <router-view style="min-height: 100vh !important;"/>

  </transition>
    <div class="bg-primary">
      <Footer></Footer>
    </div>
  </div>

</template>

<script>

import axios from 'axios';
import Navigation from "@/views/Navigation";
import Footer from "@/views/Footer";
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'
export default {
  components: {Footer, Navigation}
}

</script>
<style>
@import'~bootstrap/dist/css/bootstrap.css';
.btn-circle {
  width: 38px;
  height: 38px;
  border-radius: 19px;
  text-align: center;
  padding-left: 0;
  padding-right: 0;
  /*font-size: 16px;*/
  margin-left: 10px;
}
.form-block{
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  background-color: #f7f7f7;
  padding-left: 20%;
  padding-right: 20%;
  padding-top: 5%;
}


.moveInUp-enter-active{
  animation: fadeIn 1s ease-in;
}
@keyframes fadeIn{
  0%{
    opacity: 0;
  }
  50%{
    opacity: 0.5;
  }
  100%{
    opacity: 1;
  }
}

.navbar-nav > li{
}
.navbar {
  margin-bottom: 0;
}
.album {
  min-height: 50rem; /* Can be removed; just added for demo purposes */
  padding-top: 3rem;
  padding-bottom: 3rem;
  background-color: #f7f7f7;
}

.card {
  float: left;
  width: 33.333%;
  padding: .75rem;
  margin-bottom: 2rem;
  border: 0;
}

.card > img {
  margin-bottom: .75rem;
}

.card-text {
  font-size: 85%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.projectCard {
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;

  width: 250px;
  margin-left: 15px;
  margin-bottom: 15px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  background-color: white;
  border: solid white;
  transition: 1s;
}
.projectCard:hover{
  transform: scale(1.04);
}
.card-text{
  text-align: center;

}

a .card-body {
  color:#6c757d;
  text-decoration:none !important;

}
a:hover{
  text-decoration:none;
}
div.col-md-4{
  transition: 1s;
}
div.col-md-4:hover{
  transform: scale(1.04);
}
.container{
  display: flex;
  /*justify-content: center;*/
  flex-wrap: wrap;

}
</style>
