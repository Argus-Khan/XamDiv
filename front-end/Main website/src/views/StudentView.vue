<template>

<v-layout class="h-100" style="background-color: aliceblue; z-index: 10;">
      
    <v-container style="position: absolute; left: 0; top: 0; width: 100px; height: 100px;"><Note/></v-container>

    <NavBar class="bg-grey-darken-3"/>
      
        <v-main>

          <v-container fluid class="h-100 pa-0 ma-0">

            <v-row class="bg-grey-darken-3 pa-0 ma-0">
              <v-col align="right" class="v-col-1 offset-0">
                  <v-btn variant="tonal" rounded>
                     Note
                  </v-btn>
              </v-col>
              <v-col align="center" class="v-col-2 offset-4">
                <Counter/>
              </v-col>
              <v-col align="center" class="v-col-1 offset-3">
                  <v-btn variant="tonal" rounded>
                     Compile (3)
                  </v-btn>
              </v-col>
              <v-col align="center" class="v-col-1 offset-0">
                  <v-btn variant="tonal" rounded @click="ToggleShow()">
                     Submit
                  </v-btn>
              </v-col>
            </v-row>
  
            <v-row class="h-75 pa-5 ma-0 bg-blue-grey-darken-4" fluid>
              <v-col class="pa-4 ma-0 bg-blue-grey-darken-3 rounded-xl" v-show="ShowQuestion">
                <QuestionItem/>
              </v-col>
              <v-col class="h-100 pa-0 ma-0" fluid>
                <Editor v-show="true"/>
              </v-col>
            </v-row>

            <v-row class="h-100 pa-0 ma-0" fluid>
              <Console v-show="true"/> <!-- THIS COULD CAUSE AN UNNECESSARY SCROLLBAR -->
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
import QuestionItem from "../components/QuestionItem.vue"

export default defineComponent({
    name: 'StudentPageView',
  
    components: {
        NavBar,
        Counter,
        Editor,
        Console,
        Note,
        QuestionItem
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