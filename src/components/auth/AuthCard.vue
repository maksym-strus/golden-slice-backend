<template>
  <v-card
      elevation="2"
      outlined
      :height="height">
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
    },
    height: {
      type: Number,
      default: 500
    }
  }
}
</script>

<style scoped>

</style>
