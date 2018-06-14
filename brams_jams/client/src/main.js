import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router';
import store from './store/store.js';
import Login from './components/auth/Login.vue';
import SignUp from './components/auth/SignUp.vue';
import SongManagerHome from './components/song_manager/Home.vue';

Vue.config.productionTip = false;

Vue.use(VueRouter);

const routes = [
    { path: '/login', component: Login },
    { path: '/sign-up', component: SignUp },
    { path: '/song_manager', component: SongManagerHome },
]

export const router = new VueRouter({
  routes
});

const app = new Vue({
  el: '#app',
  store,
  router: router,
  render: h => h(App)
});

