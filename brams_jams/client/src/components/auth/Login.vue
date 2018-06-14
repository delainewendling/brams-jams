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
                  placeholder="Enter your email"
                  v-model="credentials.email"
                >
            </label>
        </div>
        <div class="form-group">
            <label for="password-input">
                Password
                <input
                  id="password-input"
                  type="password"
                  class="form-control"
                  placeholder="Enter your password"
                  v-model="credentials.password"
                >
            </label>
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
          email: '',
          password: ''
        },
        error: ''
      }
    },
    methods: {
      submit() {
        // We need to pass the component's this context
        // to properly make use of http in the auth service
        // TODO: call to backend to log user in
        axios.post("http://localhost:8000/accounts/login", this.credentials)
        .then(response => {
            console.log("")
        })
        .catch(error => {
            console.log("there was an error")
        });
      }
    }
  }
</script>