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
      ],
      FullCode: ''
    }
  },
  props: ['QuestionNumber', 'SubmitExam', 'Compiling', 'ExamID', 'StdID', 'SubmitQuestion', 'Countdown'],
  watch: {
    Compiling: function() {
      axios.post('http://localhost:8000/api/compileTest', {
        Exam_Id: this.ExamID,
        Std_Id: this.StdID,
        Q_Num: this.QuestionNumber,
        Code: JSON.stringify(this.EditorList[this.QuestionNumber - 1])
      }).then((response) => {
        this.$emit('CompileFinish', response.data)
      })
    },
    SubmitExam: function() {
      this.FullCode = (JSON.stringify(this.EditorList[0]) + '`' + JSON.stringify(this.EditorList[1]) + '`' + JSON.stringify(this.EditorList[2]) + '`' + JSON.stringify(this.EditorList[3]) + '`' + JSON.stringify(this.EditorList[4])).replaceAll('"', '')
      console.log(this.FullCode)
      axios.post('http://localhost:8000/api/submitExam', {
        Exam_Id: this.ExamID,
        Std_Id: this.StdID,
        Sub_time: String(this.Countdown),
        Code: this.FullCode
      })
      .then((response)=>{console.log(response)})
      .catch((error)=>{console.log(error)})
    }
  }
}
</script>