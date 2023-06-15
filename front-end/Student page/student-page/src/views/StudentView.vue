<template>

<v-layout class="h-100" style="background-color: aliceblue; z-index: 10;">
      
    <v-container style="position: absolute; left: 0; top: 0; width: 100px; height: 100px;"><Note/></v-container>

    <NavBar style="background-color: blueviolet;"/>
      
        <v-main>

          <v-container fluid class="h-100 pa-0 ma-0" style="background-color: green;">

            <v-row>
              <v-col align="center" class="v-col-2 offset-5 pa-5">
                <Counter/>
              </v-col>
              <v-col align="right" class="v-col-1 offset-3 pa-5">
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
              <v-col align="center" v-show="ShowQuestion" style="background-color: grey;">
                QUESTION SECTION
              </v-col>
              <v-col align="center" style="background-color: white;">
                <!-- EDITOR SECTION -->
                <Editor/>
                <Console/>
              </v-col>           
            </v-row>
  
          </v-container>
          
        </v-main>
    
    </v-layout>
    
</template>


<script>
import { defineComponent } from 'vue';
import NavBar from "../components/NavBar.vue"
import Counter from "../components/CounterItem.vue"
import Editor from "../components/CodeEditor.vue"
import Console from "../components/ConsoleOutput.vue"
import Note from "../components/ProfessorNote.vue"

export default defineComponent({
    name: 'StudentPageView',
  
    components: {
        NavBar,
        Counter,
        Editor,
        Console,
        Note
    },

    data() {
        return {
            ShowQuestion: true,
            QuestionID: 1
        }
    },
    methods: {
        ToggleShow() {
            this.ShowQuestion = !this.ShowQuestion
        }
    }
});
</script>