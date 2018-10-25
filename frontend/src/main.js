import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import VueSocketio from 'vue-socket.io'
import Notifications from 'vue-notification'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

//-----------------
//   Components
//-----------------
import Form from './components/Form'
import Board from './components/Board'


//--------------------
//  Global Variables
//--------------------
// const apiUrl = 'http://localhost:5500'
const apiUrl = 'http://gala.hartfordcitymission.org'
Vue.prototype.$apiUrl = apiUrl
Vue.prototype.$goalAmount = 20000


//---------------------
//  Set up libraries
//---------------------
Vue.use(BootstrapVue)
Vue.use(VueRouter)
Vue.use(VueSocketio, apiUrl)
Vue.use(Notifications)


//-----------
//  Routes
//-----------
var router = new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Form',
      component: Form,
    },
    {
      path: '/board',
      name: 'Board',
      component: Board,
    }
  ]
});

new Vue({
  el: '#app',
  render: h => h(App),
  router
})
