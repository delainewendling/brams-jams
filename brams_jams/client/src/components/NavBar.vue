<template>
    <div>
        <loading :show="loading"></loading>
        <a :href="logOutUrl" class="pull-right logout"> Logout </a>
    </div>
</template>

<script>
import Loading from './common/Loading.vue'
import {mapGetters} from 'vuex';
    export default {
        components: {Loading},
        computed: {
            logOutUrl () {
                return "http://localhost:8000/logout/";
            },
            ...mapGetters({
                user: 'getCurrentUser',
                loading: 'loading'
            })
        },
        beforeCreate(){
            this.$store.dispatch('getCurrentUser')
        }
    }
</script>

<style>
    .logout {
        display: inline-block;
    }
</style>