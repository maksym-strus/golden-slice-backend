<template>
  <v-card
      elevation="2"
      height="500"
      outlined>
    <v-container
        class="pa-10">
      <v-row
          align="center"
          justify="center">
        <v-col cols="12" class="text-center">
          <span :style="{fontSize: 32 + 'px'}">{{ title }}</span>
        </v-col>
      </v-row>

      <slot/>

    </v-container>
  </v-card>
</template>

<script>
export default {
  name: "AuthCard",
  props: {
    title: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>

</style>