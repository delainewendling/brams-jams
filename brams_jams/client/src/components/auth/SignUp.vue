<template>
    <div>
        <h2>Sign Up</h2>
        <p> * All fields are required </p>
         <div class="form-group">
            <label for="first-name-input">
                First Name
                <input
                  id="first-name-input"
                  type="text"
                  class="form-control"
                  v-model="user_data.first_name"
                >
            </label>
            <p class="error" v-show="error.first_name">
                {{error.first_name}}
            </p>
        </div>
         <div class="form-group">
            <label for="last-name-input">
                Last Name
                <input
                  id="last-name-input"
                  type="text"
                  class="form-control"
                  v-model="user_data.last_name"
                >
            </label>
            <p class="error" v-show="error.last_name">
                {{error.last_name}}
            </p>
        </div>
        <div class="form-group">
            <label for="email-input">
                Email
                <input
                  id="email-input"
                  type="email"
                  class="form-control"
                  v-model="user_data.email"
                >
            </label>
            <p class="error" v-show="error.email">
                {{error.email}}
            </p>
        </div>
        <div class="form-group">
            <label for="password-1-input">
                Password
                <input
                  id="password-1-input"
                  type="password"
                  class="form-control"
                  v-model="user_data.password"
                >
            </label>
            <p class="error" v-show="error.password">
                {{error.password}}
            </p>
        </div>
        <div class="form-group">
            <label for="password-2-input">
                Re-enter Password
                <input
                  id="password-2-input"
                  type="password"
                  class="form-control"
                  v-model="password2"
                >
            </label>
            <p class="error" v-show="error.password2">
                {{error.password2}}
            </p>
        </div>
        <button class="sign-up-btn" @click="submit()">Sign up</button>
        <p class="error" v-show="form_error">
                {{form_error}}
            </p>
        <div>
            <h5> Already have an account? </h5>
            <router-link to="/login">Login here</router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            user_data: {
                first_name: '',
                last_name: '',
                email: '',
                password: '',
            },
            password2: '',
            error: {
                first_name: '',
                last_name: '',
                email: '',
                password: '',
                password2: ''
            },
            form_error: '',
        }
    },
    methods: {
        resetFields(object){
            Object.keys(object).forEach(key => {
                object[key] = '';
            });
        },
        checkFields(){
            if (!this.user_data.first_name.replace(" ", "")) {
                this.error.first_name = 'You must enter a first name';
            }
            if (!this.user_data.last_name.replace(" ", "")) {
                this.error.last_name = 'You must enter a last name';
            }
            let email_parts = this.user_data.email.split('@');
            if (!this.user_data.email.replace(" ", "") || email_parts.length < 2) {
                this.error.email = 'You must enter a valid email address';
            }
            if (!this.user_data.password.replace(" ", "")) {
                this.error.password = 'You must enter a password';
            }
            if (!this.password2.replace(" ", "")) {
                this.error.password2 = 'You must re-enter your password';
            }
            if (this.user_data.password != this.password2) {
                this.error.password2 = 'Your passwords must match';
            }
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
        submit() {
            // TODO: validate user data, first name, last name, email, and passwords are the same
            this.form_error = '';
            this.resetFields(this.error);
            this.checkFields();
            // We need to pass the component's this context
            // to properly make use of http in the auth service
            // TODO: call to backend to log user in
            if (this.formIsValid()) {
                this.user_data.username = this.user_data.email;
                axios.post("http://localhost:8000/accounts/sign-up", this.user_data)
                .then(response => {
                    let credentials = {
                        username: this.user_data.email,
                        password: this.user_data.password,
                    }
                    axios.post("http://localhost:8000/api/auth/token/obtain/", credentials)
                    .then(response => {
                        console.log("credentials ", response);
                        this.resetFields(this.credentials);
                    })
                    .catch(error => {
                        console.log("there was an error");
                    });
                })
                .catch(error => {
                    console.log("error ", error['password'])
//                    this.resetFields(this.user_data);
//                    this.password2 = '';
                });
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