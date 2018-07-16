import Vue from 'vue';
import Vuex from 'vuex';
import * as types from './mutation-types';
import {axiosHelpers} from '../helpers/axiosHelpers.js';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

const state = {
    message: '',
    message_type: '',
    user: null,
    loading: false,
}

const getters = {
    message: state => state.message,
    message_type: state => state.message_type,
    loading: state => state.loading,
}

const mutations = {
    [types.SET_MESSAGE] (state, message) {
        state.message = message
    },
    [types.SET_MESSAGE_TYPE] (state, message_type) {
        state.message_type = message_type
    },
    [types.SET_CURRENT_USER] (state, user) {
        state.loading = false;
        state.user = user;
    },
    [types.PENDING_AXIOS_CALL] (state, pending_status) {
        state.loading = pending_status
    }
}

const actions = {
    setMessage ({ commit }, message, message_type) {
        commit(types.SET_MESSAGE, { message });
//        commit(types.SET_MESSAGE_TYPE, { message_type });
    },
//    setCookie ({commit}, token) {
//        // TODO: make sure this is secure
//        console.log("what is the access token? ", token.token.data.access);
//        document.cookie = `jwt_access = ${token.token.data.access};`;
//        document.cookie = `jwt_refresh = ${token.token.data.refresh};`;
//        commit(types.LOGIN_USER);
//    },
    getCurrentUser({commit}) {
        commit(types.PENDING_AXIOS_CALL, true)
        axiosHelpers.getRequest('http://localhost:8000/accounts/users/0/get_user')
        .then((user) => {
            console.log("what is the user? ", user)
            const isAuthenticated = Object.keys(user.data).length > 0;
            if (isAuthenticated) {
                commit(types.SET_CURRENT_USER, user.data);
            } else {
                window.location.href = "http://localhost:8000/login/";
            }
        })
        .catch((err) => console.log(err));
    }
}

export default new Vuex.Store({
    state,
    getters,
    mutations,
    actions,
    plugins: [createPersistedState({
        storage: window.sessionStorage,
        reducer: state => ({
          user: state.user
        })
    })]
});
