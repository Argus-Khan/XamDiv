<template>

<v-layout class="h-100" style="background-color: aliceblue; z-index: 10;">
      
    <v-container style="position: absolute; left: 0; top: 0; width: 100px; height: 100px;"><Note/></v-container>

    <NavBar class="bg-purple-darken-4"/>
      
        <v-main>

          <v-container fluid class="h-100 pa-0 ma-0 bg-purple-darken-4">

            <v-row>
              <v-col align="center" class="v-col-2 offset-5 pa-5">
                <Counter/>
              </v-col>
              <v-col align="right" class="v-col-1 offset-3 pa-5">
                  <v-btn variant="tonal" rounded>
                     Note
                  </v-btn>
              </v-col>
              <v-col align="center" class="v-col-1 offset-0 pa-5">
                  <v-btn variant="tonal" rounded @click="ToggleShow()">
                     Submit
                  </v-btn>
              </v-col>
            </v-row>
  
            <v-row class="h-100 pa-0 ma-0" fluid style="background-color: violet;">
              <v-col align="center" class="pa-0 ma-0 bg-purple-darken-1" v-show="ShowQuestion">
                QUESTION SECTION
              </v-col>
              <v-col class="pa-0 ma-0" style="background-color: gold;">
                <Editor/>
                <Console/> <!-- THIS COULD CAUSE AN UNNECESSARY SCROLLBAR -->
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

<!-- <style>
* { border: red solid 1px;}
</style> -->