<template>
  <auth-card title="Login" :height="550" :loading="loading">
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

          <div v-if="error">
            <span class="red--text">{{error.detail}}</span>
          </div>

          <v-btn
              type="submit"
              color="primary"
              class="mt-4"
              height="50"
              width="100%"
          >
            Login
          </v-btn>

          <div class="mt-5">
            <span :style="{fontSize: 16 + 'px'}">Don't have an account yet?
              <router-link to="register">Register</router-link>
            </span>
          </div>

        </form>
      </v-col>
    </v-row>
  </auth-card>
</template>

<script>
import AuthCard from '../components/auth/AuthCard';
import { validationMixin } from 'vuelidate'
import { required, maxLength, minLength } from 'vuelidate/lib/validators'

import server from '../utils/server-api'

export default {
  name: 'Login',
  mixins: [validationMixin],
  components: {
    AuthCard
  },
  data: () => ({
    username: '',
    password: '',
    error: null,
    loading: false
  }),
  validations: {
    username: { required, maxLength: maxLength(10) },
    password: { required, minLength: minLength(8) }
  },
  computed: {
    usernameErrors() {
      const errors = []
      if (!this.$v.username.$dirty) return errors
      !this.$v.username.maxLength && errors.push('Max length of username must be 10 symbols')
      !this.$v.username.required && errors.push('Username is required')
      return errors
    },
    passwordErrors() {
      const errors = []
      if (!this.$v.password.$dirty) return errors
      !this.$v.password.minLength && errors.push('Min length of password must be 8 symbols')
      !this.$v.password.required && errors.push('Password is required')
      return errors
    },
  },
  methods: {
    submit() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.loading = true

        server.post('/auth/login', {
          username: this.username,
          password: this.password,
        })
          .then((res) => {
            const { access, refresh } = res.data

            localStorage.setItem('accessToken', access)
            localStorage.setItem('refreshToken', refresh)

            this.$store.dispatch('setAuth', true)

            this.$router.push({name: 'Main'})
          })
          .catch((err) => {
            this.error = err.response.data
          })
        .finally(() => {
            this.loading = false
        })
      }
    }
  }
}
</script>
