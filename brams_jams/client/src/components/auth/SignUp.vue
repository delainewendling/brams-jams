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
                  v-model="first_name"
                >
            </label>
        </div>
         <div class="form-group">
            <label for="last-name-input">
                Last Name
                <input
                  id="last-name-input"
                  type="text"
                  class="form-control"
                  v-model="last_name"
                >
            </label>
        </div>
        <div class="form-group">
            <label for="email-input">
                Email
                <input
                  id="email-input"
                  type="email"
                  class="form-control"
                  v-model="email"
                >
            </label>
        </div>
        <div class="form-group">
            <label for="password-1-input">
                Password
                <input
                  id="password-1-input"
                  type="password"
                  class="form-control"
                  v-model="password1"
                >
            </label>
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
        </div>
        <button class="sign-up-btn" @click="submit()">Sign up</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            first_name: '',
            last_name: '',
            email: '',
            password1: '',
            password2: '',
            error: ''
        }
    },
    methods: {
        submit() {
            // TODO: validate user data, first name, last name, email, and passwords are the same
            // TODO: if it all passes then create user data object and make axios call
            let user_data = {
              first_name: this.first_name,
              last_name: this.last_name,
              email: this.email,
              password: this.password1
            }
            // We need to pass the component's this context
            // to properly make use of http in the auth service
            // TODO: call to backend to log user in
            axios.post("http://localhost:8000/accounts/sign-up", user_data)
            .then(response => {
                console.log("")
            // TODO: redirect to songs page
            })
            .catch(error => {
                console.log("there was an error")
            });
        }
    }
}

</script>