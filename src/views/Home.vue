<template>
  <v-container>
     <v-row
      align="center"
      justify="center">
       <v-col cols="12" class="text-center">
         <h2>Enter your formula</h2>
       </v-col>

       <v-col cols="10">
          <v-text-field
            placeholder="Formula">
          </v-text-field>
       </v-col>

       <v-col cols="3">
         <v-text-field
             placeholder="Point A:"
             type="number">
         </v-text-field>
       </v-col>

       <v-col cols="3">
         <v-text-field
             placeholder="Point B:"
             type="number">
         </v-text-field>
       </v-col>

       <v-col cols="3">
         <v-text-field
             placeholder="Accuracy"
             type="number">
         </v-text-field>
       </v-col>

       <v-col cols="6">
         <v-btn
             height="50"
             width="100%"
             color="secondary">
           Calculate
         </v-btn>
       </v-col>
     </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Home'
}
</script>
