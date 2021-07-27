<template>
  <div id="snippetContent">
      <div class="main-body">
        <h2>Профиль</h2>
        <div class="row gutters-sm">
          <div class="col-md-4 mb-3">
            <div class="profileCard">
              <div class="card-body">
                <div class="d-flex flex-column align-items-center text-center">
                  <img v-bind:src="icon" alt="Admin" class="rounded-circle" width="150">
                  <div class="mt-3">
                    <h4>@{{username}}</h4>
                    <p class="text-secondary mb-1">{{fullName}}</p>
                    <button class="btn btn-primary">Follow</button> <button class="btn btn-outline-primary">Змінити</button>
                  </div>
                </div>
              </div>
            </div>
            <div class="profileCard mt-3">
              <ul class="list-group list-group-flush">
                <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                  <h6 class="mb-0">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-twitter mr-2 icon-inline text-info">
                      <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
                    </svg>
                    Twitter
                  </h6>
                  <span class="text-secondary">@bootdey</span>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                  <h6 class="mb-0">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-facebook mr-2 icon-inline text-primary">
                      <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                    </svg>
                    Facebook
                  </h6>
                  <span class="text-secondary">bootdey</span>
                </li>
              </ul>
            </div>
          </div>
          <div class="col-md-8">
            <div class="profileCard mb-3">
              <div class="card-body">
                <div class="row">
                  <div class="col-sm-3">
                    <h6 class="mb-0">Full Name</h6>
                  </div>
                  <div class="col-sm-9 text-secondary"> Kenneth Valdez</div>
                </div>
                <hr>
                <div class="row">
                  <div class="col-sm-3">
                    <h6 class="mb-0">Email</h6>
                  </div>
                  <div class="col-sm-9 text-secondary">{{email}}</div>
                </div>
                <hr>
                <div class="row">
                  <div class="col-sm-3">
                    <h6 class="mb-0">expire_date</h6>
                  </div>
                  <div class="col-sm-9 text-secondary">{{expire_date}}</div>
                </div>
                <hr>
                <div class="row">
                  <div class="col-sm-3">
                    <h6 class="mb-0">firstConnection_date</h6>
                  </div>
                  <div class="col-sm-9 text-secondary">{{firstConnection_date}}</div>
                </div>

              </div>
            </div>
            <div class="row gutters-sm">
              <div class="col-sm-6 mb-3">
                <div class="profileCard h-100">
                  <div class="card-body">
                    <h6 class="d-flex align-items-center mb-3"><i class="material-icons text-info mr-2">assignment</i>Project Status</h6>
                    <small>Web Design</small>
                    <div class="progress mb-3" style="height: 5px">
                      <div class="progress-bar bg-primary" role="progressbar" style="width: 80%" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <small>Website Markup</small>
                    <div class="progress mb-3" style="height: 5px">
                      <div class="progress-bar bg-primary" role="progressbar" style="width: 72%" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <small>One Page</small>
                    <div class="progress mb-3" style="height: 5px">
                      <div class="progress-bar bg-primary" role="progressbar" style="width: 89%" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <small>Mobile Template</small>
                    <div class="progress mb-3" style="height: 5px">
                      <div class="progress-bar bg-primary" role="progressbar" style="width: 55%" aria-valuenow="55" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <small>Backend API</small>
                    <div class="progress mb-3" style="height: 5px">
                      <div class="progress-bar bg-primary" role="progressbar" style="width: 66%" aria-valuenow="66" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>

  import axios from 'axios'
  axios.defaults.xsrfHeaderName = 'X-CSRFToken'
  axios.defaults.xsrfCookieName = 'csrftoken'
   export default {
    name: 'Account',
    data () {
      return {
        fullName: '',
        email: '',
        username: '',
        password: '',
        confirm: '',
        expire_date: '',
        firstConnection_date: '',
        icon: '',
}
},
    mounted() {
      this.returnUserInformation();

    },
    methods: {
    returnUserInformation () {
      axios.post('returnUserInformation', {
        params: {
        userStatus: this.userStatus,
        email: this.email,
        username: this.username,
        fullName: this.fullName,
        expire_date: this.expire_date,
        firstConnection_date: this.firstConnection_date,
        icon: this.icon,

}}).then(response => {
    this.userStatus = response.data["userStatus"];
    this.username = response.data["username"];
    this.fullName = response.data["fullName"];
    this.email = response.data["email"];
    this.expire_date = response.data["expire_date"];
    this.firstConnection_date = response.data["firstConnection_date"];
    this.icon = response.data["icon"];
  }).catch(() => {
    console.warn('Not good man :(');
  })
}
}
}

</script>

<style scoped>
body{
  margin-top:20px;
  color: #1a202c;
  text-align: left;
  background-color: #e2e8f0;
}
.main-body{
  background-color: #f7f7f7;
}
.main-body {
  padding: 15px;
}
.profileCard {
  box-shadow: 0 1px 3px 0 rgba(0,0,0,.1), 0 1px 2px 0 rgba(0,0,0,.06);
}

.profileCard {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 0 solid rgba(0,0,0,.125);
  border-radius: .25rem;
}

.card-body {
  flex: 1 1 auto;
  min-height: 1px;
  padding: 1rem;
}

.gutters-sm {
  margin-right: -8px;
  margin-left: -8px;
}

.gutters-sm>.col, .gutters-sm>[class*=col-] {
  padding-right: 8px;
  padding-left: 8px;
}
.mb-3, .my-3 {
  margin-bottom: 1rem!important;
}

.bg-gray-300 {
  background-color: #e2e8f0;
}
.h-100 {
  height: 100%!important;
}
.shadow-none {
  box-shadow: none!important;
}
</style>