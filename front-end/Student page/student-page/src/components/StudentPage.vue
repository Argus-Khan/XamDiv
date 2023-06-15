<template>
  <v-layout class="h-100" style="background-color: aliceblue;">
    
    <NavBar style="background-color: blueviolet;"/>
    
      <v-main style="background-color: black;">

        <v-container fluid class="h-100 pa-0 ma-0" style="background-color: green;">
        
          <v-row>
            <v-col align="center" class="v-col-1 offset-9 pa-5">
              <Counter/>
            </v-col>
            <v-col align="right" class="v-col-1 offset-0 pa-5">
                <v-btn variant="tonal" @click="ToggleShow()">
                   Note
                </v-btn>
            </v-col>
            <v-col align="center" class="v-col-1 offset-0 pa-5">
                <v-btn variant="tonal" @click="ToggleShow()">
                   Submit
                </v-btn>
            </v-col>
          </v-row>

          <v-row class="h-100 ma-0" style="background-color: aquamarine;">
            <v-col align="center" v-show="ShowToggle" style="background-color: grey;">
              QUESTION SECTION
            </v-col>
            <v-col align="center" style="background-color: white;">
              EDITOR SECTION
            </v-col>           
          </v-row>

        </v-container>
        
      </v-main>
  
  </v-layout>
</template>

<script setup>
  import NavBar from "./NavBar.vue"
  import Counter from "./CounterItem.vue"
</script>

<script>
    export default {
        data() {
            return {
                ShowToggle: true
            }
        },
        methods: {
            ToggleShow() {
                this.ShowToggle = !this.ShowToggle
            }
        }
    }
</script>

<style>
  html {
    overflow-y: hidden !important;
}
</style>