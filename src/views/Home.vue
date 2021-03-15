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

         <v-col cols="3">
           <v-text-field
               v-model="pointA"
               placeholder="Point A:"
               type="number"
               :rules="[v => !!v || 'It\'s not can be empty']">
           </v-text-field>
         </v-col>

         <v-col cols="3">
           <v-text-field
               v-model="pointB"
               placeholder="Point B:"
               type="number"
               :rules="[v => !!v || 'It\'s not can be empty', v => v > pointA || 'Point B must be bigger than A']">
           </v-text-field>
         </v-col>

         <v-col cols="3">
           <v-text-field
               v-model="accuracy"
               placeholder="Accuracy"
               type="number"
               :rules="[v => !!v || 'It\'s not can be empty', v => 0 < v && v < 1 || 'Accuracy must be in range from 0 to 1']">
           </v-text-field>
         </v-col>

         <v-col cols="6">
           <v-btn
               type="submit"
               height="50"
               width="100%"
               color="secondary">
             Calculate
           </v-btn>
         </v-col>


     </v-row>

  </v-container>
  </v-form>
</template>

<script>
import server from "@/utils/server-api";

export default {
  name: 'Home',
  data: () => ({
    formula: null,
    pointA: null,
    pointB: null,
    accuracy: null
  }),
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        server.post('/graphic', {
          formula: this.formula,
          start_point: this.pointA,
          end_point: this.pointB,
          accuracy: this.accuracy
        })
        .then((res) => {
          const newId = res.data.id

          this.$router.push(`/result/${newId}`)
        })
        .catch(() => {})
      }
    }
  }
}
</script>
