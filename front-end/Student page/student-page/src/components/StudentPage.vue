<template>
  <v-layout class="h-100" style="background-color: aliceblue;">
    <NavBar style="background-color: blueviolet;"/>
      <v-main style="background-color: black;">

        <!-- <v-container class="" fluid style="background-color: beige;">
          <Counter/>
          Testing the bounds of this litte thingy
        </v-container> -->

        <v-container fluid class="h-100 pa-0 ma-0" style="background-color: antiquewhite;">
        <v-row>
            <v-col align="center" class="v-col-2 offset-5 pa-5">
                <v-btn variant="tonal" @click="ToggleShow()">
                   Toggle fullscreen
                </v-btn>
            </v-col>
        </v-row>
        <v-row class="h-100 ma-0" style="background-color: aquamarine;">
            <v-col align="center" v-show="ShowToggle" style="background-color: cyan;">
                Hello There
            </v-col>
            <v-col align="center" style="background-color: white;">
                <v-textarea label="Code editor"></v-textarea>
                <v-divider></v-divider>
                <div class="pa-4 text-end">
                    <v-btn
                        class="text-none"
                        color="medium-emphasis"
                        min-width="92"
                        rounded
                        variant="outlined"
                        @click="dialog = false"
                    >
                        Submit
                    </v-btn>
                </div>
            </v-col>
        </v-row>
    </v-container>
      </v-main>
  </v-layout>
</template>

<script setup>
  import NavBar from "./NavBar.vue"
  // import Counter from "./CounterItem.vue"
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