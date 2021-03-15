<template>
  <auth-card title="Register" :height="1000">
    <v-row
        justify="start"
        align="start">
      <v-col col="6">

        <form @submit.prevent="submit">

          <span class="font-weight-bold" :style="{fontSize: 20 + 'px'}">Username</span>
          <v-text-field
              v-model="username"
              placeholder="Your username"
              outlined
              clearable
              :error-messages="usernameErrors"
              :error="!!usernameErrors.length"
          ></v-text-field>

          <span class="font-weight-bold" :style="{fontSize: 20 + 'px'}">Password</span>
          <v-text-field
              v-model="password"
              placeholder="Your password"
              type="password"
              outlined
              clearable
              :error-messages="passwordErrors"
              :error="!!passwordErrors.length"
          ></v-text-field>

          <span class="font-weight-bold" :style="{fontSize: 20 + 'px'}">Repeat password</span>
          <v-text-field
              v-model="password2"
              placeholder="Repeat your password"
              type="password"
              outlined
              clearable
              :error-messages="password2Errors"
              :error="!!password2Errors.length"
          ></v-text-field>

          <span class="font-weight-bold" :style="{fontSize: 20 + 'px'}">Email</span>
          <v-text-field
              v-model="email"
              placeholder="Your email"
              outlined
              clearable
              :error-messages="emailErrors"
              :error="!!emailErrors.length"
          ></v-text-field>

          <span class="font-weight-bold" :style="{fontSize: 20 + 'px'}">First name</span>
          <v-text-field
              v-model="firstname"
              placeholder="Your first name"
              outlined
              clearable
              :error-messages="firstnameErrors"
              :error="!!firstnameErrors.length"
          ></v-text-field>

          <span class="font-weight-bold" :style="{fontSize: 20 + 'px'}">Last name</span>
          <v-text-field
              v-model="lastname"
              placeholder="Your last name"
              outlined
              clearable
              :error-messages="lastnameErrors"
              :error="!!lastnameErrors.length"
          ></v-text-field>

          <div v-if="errors">
            <ul v-for="(error,errorName) in errors" :key="error.join('')">
              <li class="red--text" v-for="errorText of error" :key="errorText">
                {{errorName.toUpperCase()}}: {{errorText}}
              </li>
            </ul>
          </div>

          <v-btn
              type="submit"
              color="primary"
              class="mt-4"
              height="50"
              width="100%"
          >
            Register
          </v-btn>
        </form>

        <div class="mt-5">
          <span :style="{fontSize: 16 + 'px'}">Already have an account?
            <router-link to="login">Login</router-link>
          </span>
        </div>

      </v-col>
    </v-row>
  </auth-card>
</template>

<script>
import AuthCard from "../components/auth/AuthCard"
import { validationMixin } from 'vuelidate'
import { required, maxLength, minLength, email, sameAs } from 'vuelidate/lib/validators'

import server from '../utils/server-api'

export default {
  name: 'Register',
  mixins: [validationMixin],
  components: {
    AuthCard
  },

  data: () => ({
    username: '',
    password: '',
    password2: '',
    email: '',
    firstname: '',
    lastname: '',
    errors: null,
    loading: false
  }),

  validations: {
    username: { required, maxLength: maxLength(10) },
    password: { required, minLength: minLength(8) },
    password2: { sameAs: sameAs('password') },
    email: { required, email },
    firstname: { required },
    lastname: { required }
  },

  computed: {
    emailErrors () {
      const errors = []
      if (!this.$v.email.$dirty) return errors
      !this.$v.email.email && errors.push('Must be valid e-mail')
      !this.$v.email.required && errors.push('E-mail is required')
      return errors
    },
    usernameErrors () {
      const errors = []
      if (!this.$v.username.$dirty) return errors
      !this.$v.username.maxLength && errors.push('Max length of username must be 10 symbols')
      !this.$v.username.required && errors.push('Username is required')
      return errors
    },
    passwordErrors () {
      const errors = []
      if (!this.$v.password.$dirty) return errors
      !this.$v.password.minLength && errors.push('Min length of password must be 8 symbols')
      !this.$v.password.required && errors.push('Password is required')
      return errors
    },
    password2Errors () {
      const errors = []
      if (!this.$v.password2.$dirty) return errors
      !this.$v.password2.sameAs && errors.push('Repeated password must be the same as original')
      return errors
    },
    firstnameErrors () {
      const errors = []
      if (!this.$v.firstname.$dirty) return errors
      !this.$v.firstname.required && errors.push('First name is required')
      return errors
    },
    lastnameErrors () {
      const errors = []
      if (!this.$v.lastname.$dirty) return errors
      !this.$v.lastname.required && errors.push('Last name is required')
      return errors
    },
  },

  methods: {
    submit() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.loading = true

        server.post('/auth/register', {
          username: this.username,
          password: this.password,
          password2: this.password2,
          email: this.email,
          first_name: this.firstname,
          last_name: this.lastname
        })
        .then(() => {
          this.$router.push('login')
        })
        .catch((err) => {
          this.errors = err.response.data
        })
        .finally(() => {
          this.loading = false
        })
      }
    }
  }
}
</script>
