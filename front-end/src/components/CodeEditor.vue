<template>
    <v-container fluid class="pa-5 ma-0 pt-0">
      <v-textarea v-model="EditorList[QuestionNumber - 1]" class="bg-blue-grey-darken-3 rounded-xl pa-5" color="black" label="Code editor" rows="23" no-resize hide-details>
      </v-textarea>
    </v-container>
</template>

<script>
import axios from "axios"
export default {
  data() {
    return {
      EditorList: [
        '', '', '', '', ''
      ]
    }
  },
  props: ['QuestionNumber', 'Compiling', 'ExamID', 'StdID'],
  watch: {
    Compiling: function() {
      console.log(this.EditorList[this.QuestionNumber - 1])
      axios.post('http://localhost:8000/api/compileTest', {
        Exam_Id: this.ExamID,
        Std_Id: this.StdID,
        Q_Num: this.QuestionNumber,
        Code: this.EditorList[this.QuestionNumber - 1]
      }).then((response) => {
        this.$emit('CompileFinish', response.data)
      })
    }
  }
}
</script>