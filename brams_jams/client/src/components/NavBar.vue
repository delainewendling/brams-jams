<template>
    <div class="nav-bar">
        <div class="nav-bar-items">
            <div class="nav-item active">
                Your Songs
            </div>
        </div>
        <a :href="logOutUrl" class="pull-right logout"> Logout </a>
        <loading :show="loading"></loading>
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
    .nav-bar-items {
        display: flex;
        flex-grow: 3;
        text-align: left;
    }
    .nav-bar {
        display: flex;
        background-color: #eee;
    }
    .active {
        border-bottom: solid 2px #10A0FF;
    }
    .nav-item {
        color: #777;
        padding: 15px;
        cursor: pointer;
        margin-left: 8px;
    }
</style>