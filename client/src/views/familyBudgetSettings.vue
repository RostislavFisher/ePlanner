<template>
  <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="row" style="text-align: left; margin-right: 0px; margin-left: 0px;">
      <div>

        <h1 class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom" >Планировка месячного бюджета</h1>

      </div>
    </div>
    <div>
      <input type="text" class="form-control" placeholder="Мой месячный бюджет" aria-label="Мой месячный бюджет" aria-describedby="basic-addon2" ref="budget" v-model="totalBudget" style="margin-bottom: 100px;">
    </div>

    <div>
      <div class="input-group mb-3" v-for="item in budgetItems" v-bind:key="item">
        <input type="text" class="form-control" placeholder="Тип покупки" aria-label="Тип покупки" aria-describedby="basic-addon2" ref="type" v-bind:value="item[0]">
        <input type="number" class="form-control" placeholder="Ограничение количества" aria-label="Ограничение количества" aria-describedby="basic-addon2" ref="limit" v-bind:value="item[1]">
      </div>

      <button type="button" class="btn btn-secondary" @click="addToItems">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
          <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"></path>
        </svg>
      </button>
      <button type="button" class="btn btn-primary" @click="save">Сохранить</button>

    </div>

    <div>
      <div style="display: flex; justify-content: space-between;">
        <div style="width: 50%;">
          <p>Распределено: 100%</p>
        </div>
        <div style="width: 33%;">
          <my-chart v-bind:TypeList="this.TypeList" v-bind:LimitList="this.LimitList"></my-chart>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import MyChart from './myChart'
import axios from "axios";

class budget {
  constructor(Type, Limit) {
    this.Type = Type;
    this.Limit = Limit;
  }
}
export default {
  name: "familyBudgetSettings",
  data() {
    return {
      countAmount: 0,
      totalBudget: 0,
      distributed: 0,
      TypeList : [],
      LimitList: [],
      MoneyLimitObject: {
        Type: "",
        Limit: "",
      },
      budgetItems: [],
    }
  },
  mounted() {
    console.log(this.budgetItems);
    axios.get("/returnBudgetOfFamily", {
      params:{
        familyID : this.$route.params.familyID,
      }
    }).then(result => {
      this.budgetItems = result.data["budgetItems"]
      this.totalBudget = result.data["totalBudget"]
      this.countAmount = result.data["budgetItems"].length;
      console.log(this.countAmount);
      console.log(this.budgetItems);
      console.log(this.totalBudget);
    })
  },
  components: {
    'my-chart': MyChart

  },
  methods: {
    addToItems() {
      this.budgetItems.push(["", ""]);
    },
    save() {
      var listOfTypeList = [];
      var listOfLimitList = [];
      for (let i = 0; i < this.$refs["type"].length; i++) {
        listOfTypeList.push(this.$refs["type"][i]["value"]);
      }
      for (let i = 0; i < this.$refs["limit"].length; i++) {
        listOfLimitList.push(parseFloat(this.$refs["limit"][i]["value"]));
      }
      this.TypeList = listOfTypeList;
      this.LimitList = listOfLimitList;

      var budgetList = [];
      for (let i = 0; i < this.$refs["type"].length; i++) {
        budgetList.push(new budget(this.$refs["type"][i]["value"], this.$refs["limit"][i]["value"]))
      }
      if("" in listOfLimitList || "" in listOfTypeList){
        alert("spaces are not allowable");
      }
      else{
        axios.get("/budgetFamilyEdit", {
          params: {
            familyID : this.$route.params.familyID,
            totalBudget: this.totalBudget,
            budgetList: budgetList
          }})
      }
    }
  }
}
</script>

<style scoped>

</style>