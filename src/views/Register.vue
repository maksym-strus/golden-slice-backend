<template>
  <auth-card title="Register">
    <v-row
        justify="start"
        align="start">
      <v-col col="6">

        <span class="font-weight-bold" :style="{fontSize: 20 + 'px'}">Username</span>
        <v-text-field
            placeholder="Your username"
            outlined
            clearable
        ></v-text-field>

        <span class="font-weight-bold" :style="{fontSize: 20 + 'px'}">Password</span>
        <v-text-field
            placeholder="Your password"
            type="password"
            outlined
            clearable
        ></v-text-field>

        <v-btn
            color="primary"
            class="mt-4"
            height="50"
            width="100%"
        >
          Register
        </v-btn>

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
import AuthCard from "../components/auth/AuthCard";

export default {
  name: 'Register',
  components: {
    AuthCard
  }
}
</script>
