<template>

<v-layout class="h-100" style="background-color: aliceblue; z-index: 10;">
  <Transition>
  <v-container fluid v-show="ShowPopup" style="position: absolute; left: 0; top: 0;  z-index: 1000; background-color: #000d;" class="h-100"><Note @close="TogglePopup()"/></v-container>
  </Transition>

    <NavBar class="bg-grey-darken-3" @ChangeQuestion="ChangeQuestion"/>
      
        <v-main>

          <v-container fluid class="h-100 pa-0 ma-0">

            <v-row class="bg-grey-darken-3 pa-0 ma-0">
              <v-col align="center" class="v-col-1 offset-0">
                  <v-btn variant="tonal" rounded @click="TogglePopup()">
                     Note
                  </v-btn>
              </v-col>
              <v-col align="center" class="v-col-2 offset-4">
                <Counter :StartCountdown="StartCountdown"/>
              </v-col>
              <v-col align="center" class="v-col-1 offset-3">
                  <v-btn :disabled="CompileDisabled[this.QuestionNumber - 1]" variant="tonal" @click="SendToCompiler" rounded>
                     Compile ({{ 3 - Compiles[this.QuestionNumber - 1]}})
                  </v-btn>
              </v-col>
              <v-col align="center" class="v-col-1 offset-0">
                  <SubmitButton/>
              </v-col>
            </v-row>
  
            <v-row class="h-75 pa-5 ma-0 bg-blue-grey-darken-4" fluid>
              <v-col class="pa-4 ma-0 bg-blue-grey-darken-3 rounded-xl" v-show="ShowQuestion">
                <QuestionItem :QuestionNumber="QuestionNumber" @CloseQuestion="ToggleQuestion()"/>
              </v-col>
              <v-col class="h-100 pa-0" fluid>
                <Editor :QuestionNumber="QuestionNumber"/>
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
import SubmitButton from "../components/SubmitButton.vue"
import axios from 'axios'

export default defineComponent({
    name: 'StudentPageView',
  
    components: {
        NavBar,
        Counter,
        Editor,
        Console,
        Note,
        QuestionItem,
        SubmitButton
    },

    data() {
        return {
            ShowQuestion: true,
            ShowPopup: true,
            QuestionNumber: 1,
            CompileDisabled: [false, false, false, false, false],
            Compiles: [0, 0, 0, 0, 0],
            StartCountdown: false,
            Exam: {
              questionsNotes: [{}],
              studentsIds: []
            },
        }
    },

    props: ['StdID', 'ExamID'],

    methods: {
        ToggleQuestion() {
          this.ShowQuestion = !this.ShowQuestion
        },
        TogglePopup() {
          this.ShowPopup = !this.ShowPopup
          this.StartCountdown = true
        },
        ChangeQuestion(num) {
          this.QuestionNumber = num
          this.ShowQuestion = true
        },
        SendToCompiler() {
          this.Compiles[this.QuestionNumber - 1]++
          if (this.Compiles[this.QuestionNumber - 1] == 3) {
            this.CompileDisabled[this.QuestionNumber - 1] = true
          }
        }
    },

    watch: {
      StdID: function(newval) {
        console.log(newval)
      }
    },

    created() {
      axios.get('http://localhost:8000/api/getExam?Exam_Id=' + this.ExamID)
      .then((request)=>{this.Exam = request.data})
    }
});
</script>

<style scoped>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>