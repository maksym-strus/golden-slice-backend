<template>
  <v-form
      ref="form"
      @submit.prevent="submit"
      lazy-validation>
  <v-container>

     <v-row
      align="center"
      justify="center">
       <v-col cols="12" class="text-center">
         <h2>Enter your formula</h2>
       </v-col>



         <v-col cols="10">
            <v-text-field
                v-model="formula"
                :rules="[v => !!v || 'It\'s not can be empty']"
              placeholder="Formula">
            </v-text-field>
         </v-col>

         <v-col cols="4">
           <v-text-field
               v-model="pointX0"
               placeholder="Point x0:"
               type="number"
               :rules="[v => !!v || 'It\'s not can be empty']">
           </v-text-field>
         </v-col>

       <v-col cols="4">
         <v-text-field
             v-model="step"
             placeholder="Step:"
             type="number"
             :rules="[v => !!v || 'It\'s not can be empty']">
         </v-text-field>
       </v-col>

         <v-col cols="4">
           <v-text-field
               v-model="accuracy"
               placeholder="Accuracy:"
               type="number"
               :rules="[v => !!v || 'It\'s not can be empty', v => 0 < v && v < 1 || 'Accuracy must be in range from 0 to 1']">
           </v-text-field>
         </v-col>

         <v-col cols="6">
           <v-btn
               type="submit"
               height="50"
               width="100%"
               color="#ebd534">
             Calculate
           </v-btn>
         </v-col>

       <v-snackbar
           v-model="isSnackbarVisible"
           :top="true"
           timeout="3000"
           color="red darken-3"
       >
         {{ errorText }}
       </v-snackbar>
     </v-row>

  </v-container>
  </v-form>
</template>

<script>
import server from '@/utils/server-api';

export default {
  name: 'Home',
  data: () => ({
    formula: null,
    pointX0: null,
    step: null,
    numberOfPoints: null,
    accuracy: null,
    errorText: null,
    isSnackbarVisible: null,
  }),
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        server.post('/graphic', {
          formula: this.formula,
          start_point: this.pointX0,
          step: this.step,
          number_of_points: 50,
          accuracy: this.accuracy
        })
        .then((res) => {
          const newId = res.data.id

          this.$router.push(`/result/${newId}`)
        })
        .catch((err) => {
          this.errorText = err.response.data;
          this.isSnackbarVisible = true;
        })
      }
    }
  }
}
</script>
