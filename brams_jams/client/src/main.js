import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router';
import store from './store/store.js';
//import Login from './components/auth/Login.vue';
//import SignUp from './components/auth/SignUp.vue';
import Login from './components/Login.vue';
import SongManagerHome from './components/song_manager/Home.vue';
import NotFoundView from './components/common/NotFound.vue';
import Buefy from 'buefy';
import 'buefy/lib/buefy.css';
import VoerroTagsInput from '@voerro/vue-tagsinput';

Vue.config.productionTip = false;

Vue.component('tags-input', VoerroTagsInput);

Vue.use(VueRouter);
Vue.use(Buefy);

const routes = [
    { path: '/login', component: Login },
    { path: '/', redirect: 'song_manager' },
    { path: '/song_manager', component: SongManagerHome },
    { path: '*', component: NotFoundView }
]

//    { path: '/login', component: Login },
//    { path: '/sign-up', component: SignUp },

export const router = new VueRouter({
  routes
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        // this route requires auth, check if logged in
        // if not, redirect to login page.
        if (!auth.loggedIn()) {
            next({
                path: '/login',
                query: { redirect: to.fullPath }
            })
        } else {
            next()
        }
    } else {
        next() // make sure to always call next()!
    }
})

const app = new Vue({
  el: '#app',
  store,
  router: router,
  render: h => h(App)
});

