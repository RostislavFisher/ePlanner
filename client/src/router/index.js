import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import budgetListOfProductsFormat from "../views/budgetListOfProductsFormat";
import budgetSettings from "../views/budgetSettings";
import budgetProducts from "../views/budgetProducts";
import budgetCreateProduct from "../views/budgetCreateProduct";
import createFamily from "../views/createFamily";
import budgetFamilyProducts from "../views/budgetFamilyProducts";
import familyBudgetSettings from "../views/familyBudgetSettings";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/Account',
    name: 'Account',

    component: () => import('../views/Account.vue')
  },
  {
    path: '/Login',
    name: 'Login',

    component: () => import('../views/Login.vue')
  },
  {
    path: '/Register',
    name: 'Register',

    component: () => import('../views/Register.vue')
  },
  {
    path: '/products',
    name: 'products',

    component: () => import('../views/budgetProducts.vue')
  },
  {
    path: '/budget',
    name: 'budget',

    component: () => import('../views/budget.vue'),
    children: [
      {
        path: '/budget/family/:familyID',
        name: 'family',

        component: () => import('../views/family.vue'),
        children: [
          {
            path: '',
            component: budgetListOfProductsFormat
          },
          {
            path: 'budgetFamilyProducts',
            component: budgetFamilyProducts
          },
          {
            path: 'familyBudgetSettings',
            component: familyBudgetSettings
          },
        ]
      },
      {
        path: '',
        component: budgetListOfProductsFormat
      },
      {
        path: 'budgetSettings',
        component: budgetSettings
      },
      {
        path: 'budgetProducts',
        component: budgetProducts
      },
      {
        path: 'budgetCreateProduct',
        component: budgetCreateProduct
      },
      {
        path: 'createFamily',
        component: createFamily
      },

    ]
  },
]

const router = new VueRouter({
  routes
})

export default router
