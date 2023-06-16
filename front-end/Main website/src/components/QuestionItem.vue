<template>
    <v-container class="pa-5 ma-0 h-100">
        <v-row class="pa-0 ma-0">
            <v-col align="center" class="v-col-11 offset-0 pa-4">
                <h2>Question {{ QuestionNumber }}</h2>
            </v-col>
            <v-col align="center" class="v-col-1 offset-0">
                <v-btn variant="tonal" rounded @click="this.$emit('CloseQuestion')">
                     X
                  </v-btn>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-divider class="border-opacity-100"></v-divider>
                    {{ QuestionList[num] }}
                <v-divider class="border-opacity-100"></v-divider>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    props: ['QuestionNumber'],
    data() {
        return {
            num: 0,
            QuestionList: [
                'jasoighioshfi;oh gfsnhf8p shfiohsf89 nhsifh9s8 hf98whf89 whfi shaiufhI LOVE fosihf shfus fiuhsfi',
                'hfsifishf sif',
                'I WILL KILL',
                'MYSELF',
                'OISJFIOSH IFOHFIHF9IUFNH'
            ]
        }
    },
    watch: {
        QuestionNumber: function(newval) {
            this.num = newval - 1
        }
    }
}
</script>