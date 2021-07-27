  <template>
  <div class="home">
    <section class="jumbotron text-center" style="background-color: white; ">
      <div class="container"></div>
      <div class="row py-lg-5">
        <div class="col-lg-6 col-md-8 mx-auto">
          <h1 class="fw-light">ua_files</h1>
          <p class="lead text-muted">ТЕКСТ</p>
          <p>
            <a href="#" class="btn btn-primary my-2">Детальнее</a>
            <a href="#" class="btn btn-secondary my-2">Зарегистрироваться</a>
          </p>
        </div>
      </div>
    </section>
    <div class="album text-muted">
      <h2 style="margin-bottom: 100px;">Последние Тарифы</h2>
      <div class="container">
        <div class="row">
          <div class="projectCard">
            <router-link to="/Tariff" class="nav-link">
              <div>
                <img class="card-img-top" src="http://s1.iconbird.com/ico/2013/9/452/w512h5121380476717calendar.png" style="height:250px;  object-fit:cover; filter: ">
              </div>
              <div class="card-body">
                <h2 class="card-text" align="center">Недельный тариф</h2>
                <p class="card-text">ТЕКСТ</p>

              </div>
            </router-link>
          </div>
          <div class="projectCard">
            <router-link to="/project" class="nav-link">
              <div>
                <img class="card-img-top" src="http://s1.iconbird.com/ico/2013/9/452/w512h5121380476717calendar.png" style="height:250px;  object-fit:cover; filter: ">
              </div>
              <div class="card-body">
                <h2 class="card-text" align="center">Месячный тариф</h2>
                <p class="card-text">ТЕКСТ</p>

              </div>
            </router-link>
          </div>
          <div class="projectCard">
            <router-link to="/project" class="nav-link">
              <div>
                <img class="card-img-top" src="http://s1.iconbird.com/ico/2013/9/452/w512h5121380476717calendar.png" style="height:250px;  object-fit:cover; filter: ">
              </div>
              <div class="card-body">
                <h2 class="card-text" align="center">Годовой тариф</h2>
                <p class="card-text">ТЕКСТ</p>

              </div>
            </router-link>
          </div>

        </div>

      </div>
    </div>



  </div>
</template>

<script>
// @ is an alias to /src
// import Home from '@/components/Home.vue'

export default {
  name: 'Home',
  components: {
    // Home
  },

}
</script>
<style>

</style>