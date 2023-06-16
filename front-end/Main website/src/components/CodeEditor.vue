<template>
    <v-container fluid class="pa-5 ma-0 pt-0">
      <v-textarea v-model="EditorList[QuestionNumber - 1]" class="bg-blue-grey-darken-3 rounded-xl pa-5" color="black" label="Code editor" rows="23" no-resize hide-details>
      </v-textarea>
    </v-container>
</template>

<script>
export default {
    data() {
      return {
        EditorList: [
          '', '', '', '', ''
        ]
      }
    },
    props: ['QuestionNumber']
}
</script>