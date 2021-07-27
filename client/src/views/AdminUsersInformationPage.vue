<template>
  <div class="table-responsive" style="padding-left: 1.5rem !important; padding-right: 1.5rem !important;">
    <table class="table table-striped table-sm">
    <thead data-v-5caa450d="">
    <tr data-v-5caa450d="">
      <th data-v-5caa450d="">Ник</th>
      <th data-v-5caa450d="">Имя</th>
      <th data-v-5caa450d="">Почта</th>
      <th data-v-5caa450d="">Дата окончания подписки</th>
      <th data-v-5caa450d="">Дата регистрации</th>
      <th data-v-5caa450d="">Детали</th>
    </tr>
    </thead>
    <tbody data-v-5caa450d="">
    <tr data-v-5caa450d="" v-for="user in listOfUsers" v-bind:key="user">
      <td data-v-5caa450d="">{{ user.username }}</td>
      <td data-v-5caa450d="">{{ user.fullName }}</td>
      <td data-v-5caa450d="">{{ user.email }}</td>
      <td data-v-5caa450d="">{{ user.expire_date }}</td>
      <td data-v-5caa450d="">{{ user.firstConnection_date }}</td>
      <td data-v-5caa450d="">
        <div class="dropdown float-right">
        <button class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots" viewBox="0 0 16 16">
            <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/>
          </svg>

        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
          <a class="dropdown-item" href="#">Змінити</a>
          <button class="dropdown-item" v-on:click="deleteAccount(user.id)" v-if="user.userStatus === 'user'">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
              <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
              <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
            </svg>
            Видалити</button>
        </div>
      </div></td>
    </tr>


    </tbody>
  </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
name: "AdminUsersInformationPage",
  data(){
  return{
    listOfUsers: ""
  }
  },
  mounted() {
  this.getUserListInformation();
  },
  methods: {
    getUserListInformation(){
      axios.post('getUserListInformation', {
      }).then((response) => {
        this.listOfUsers = response.data["data"];
      });
    },
    deleteAccount(id){
      axios.post('deleteAccount', {
        params: {
          id : id
        }
      }).then((response) =>{
        console.log(response);
        this.getUserListInformation();
      });
    },
  }
}
</script>

<style scoped>

</style>