import Vue from 'vue';
import Vuex from 'vuex';
import * as types from './mutation-types';

Vue.use(Vuex);

const state = {
    message: '',
    type: ''
}

const getters = {
    message: state => state.message,
    type: state => state.type
}

const mutations = {
    [types.SET_MESSAGE] (state, message) {
        state.message = message
    },
    [types.SET_TYPE] (state, type) {
        state.type = type
    }
}

const actions = {
    setMessage ({ commit }, message, type) {
        commit(types.SET_MESSAGE, { message })
        commit(types.SET_TYPE, { type })
    }
}

export default new Vuex.Store({
    state,
    getters,
    mutations,
    actions,
});
