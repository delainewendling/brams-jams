import Vue from 'vue';
import Vuex from 'vuex';
import * as types from './mutation-types';

Vue.use(Vuex);

const state = {
    message: '',
    message_type: '',
    is_logged_in: false,
}

const getters = {
    message: state => state.message,
    message_type: state => state.message_type
}

const mutations = {
    [types.SET_MESSAGE] (state, message) {
        state.message = message
    },
    [types.SET_MESSAGE_TYPE] (state, message_type) {
        state.message_type = message_type
    },
    [types.LOGIN_USER] (state) {
        state.is_logged_in = true;
    },
}

const actions = {
    setMessage ({ commit }, message, message_type) {
        commit(types.SET_MESSAGE, { message });
//        commit(types.SET_MESSAGE_TYPE, { message_type });
    },
    setCookie ({commit}, token) {
        // TODO: make sure this is secure
        console.log("what is the access token? ", token.token.data.access);
        document.cookie = `jwt_access = ${token.token.data.access};`;
        document.cookie = `jwt_refresh = ${token.token.data.refresh};`;
        commit(types.LOGIN_USER);
    },
}

export default new Vuex.Store({
    state,
    getters,
    mutations,
    actions,
});
