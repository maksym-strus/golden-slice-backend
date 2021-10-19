<template>
  <v-container>
    <v-row justify="center" align="center">
      <v-col cols="5" class="justify-center d-flex">
       <v-img src="../../assets/img/golden-ratio.png" />
      </v-col>
      <v-col cols="12">
         <v-list flat>
           <v-list-item-group
               v-model="selectedItem"
               color="secondary"
           >
             <v-list-item
                 v-for="(item, i) in items"
                 :key="i"
                 :to="item.link">
               <v-list-item-icon>
                 <v-icon v-text="item.icon"></v-icon>
               </v-list-item-icon>
               <v-list-item-content>
                 <v-list-item-title>
                   {{item.text}}
                 </v-list-item-title>
               </v-list-item-content>
             </v-list-item>
           </v-list-item-group>
         </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'NavBar',
  data: () => ({
    selectedItem: 1,
    items: [
      { text: 'Home', icon: 'mdi-clock', link: '/home' },
      { text: 'My calculations', icon: 'mdi-account', link: '/result' },
      { text: 'About', icon: 'mdi-flag', link: '/about' },
    ],
  })
}
</script>
