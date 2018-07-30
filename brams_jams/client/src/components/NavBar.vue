<template>
    <div class="nav-bar">
        <div class="nav-bar-items">
            <div class="nav-item active">
                Your Songs
            </div>
        </div>
        <span class="user-name"> Hey {{user.first_name}} </span>
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
                return `${this.api_host_url}/logout/`;
            },
            ...mapGetters({
                user: 'user',
                loading: 'loading',
                api_host_url: 'api_host_url'
            })
        },
        beforeCreate(){
            this.$store.dispatch('getCurrentUser')
        }
    }
</script>

<style>
    .logout,
    .user-name {
        display: inline-block;
        margin: 15px;
        color: #777;
    }
    .logout:visited {
        color: #777;
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