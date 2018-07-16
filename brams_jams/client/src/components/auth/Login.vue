<template>
    <div>
        <h2>Log In</h2>
        <div class="form-group">
            <label for="email-input">
                Email
                <input
                  id="email-input"
                  type="email"
                  class="form-control"
                  v-model="credentials.username"
                >
            </label>
            <p class="error" v-show="error.username">
                {{error.username}}
            </p>
        </div>
        <div class="form-group">
            <label for="password-input">
                Password
                <input
                  id="password-input"
                  type="password"
                  class="form-control"
                  v-model="credentials.password"
                >
            </label>
            <p class="error" v-show="error.password">
                {{error.password}}
            </p>
        </div>
        <button class="login-btn" @click="submit()">Login</button>
        <div>
            <h5> Don't have an account yet? </h5>
            <router-link to="/sign-up">Sign up here</router-link>
        </div>
    </div>
  </template>

<script>
import axios from 'axios';
  export default {
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        },
        error: {
          username: '',
          password: '',
        }
      }
    },
    methods: {
        resetFields(object){
            Object.keys(object).forEach(key => {
                object[key] = '';
            });
        },
        formIsValid(){
            let is_valid = true;
            Object.keys(this.error).forEach(key => {
                if (this.error[key] != '') {
                    is_valid = false;
                }
            })
            return is_valid;
        },
        checkFields(){
            let email_parts = this.credentials.username.split('@');
            if (!this.credentials.username.replace(" ", "") || email_parts.length < 2) {
                this.error.username = 'You must enter a valid email address';
            }
            if (!this.credentials.password.replace(" ", "")) {
                this.error.password = 'You must enter a password';
            }
        },
        submit() {
            this.resetFields(this.error);
            this.checkFields();
            // We need to pass the component's this context
            // to properly make use of http in the auth service
            // TODO: call to backend to log user in
            if (this.formIsValid()){
                axios.post("http://localhost:8000/api/auth/token/obtain/", this.credentials)
                .then(response => {
                    this.resetFields(this.credentials);
                    this.$store.dispatch('setCookie', {token: response})
                    this.$router.push('/song_manager');
                })
                .catch(error => {
                    console.log("there was an error");
                })
            }
        }
    }
  }
</script>

<style scoped>
.error {
    color: red;
    font-size: 0.75em;
}
</style>