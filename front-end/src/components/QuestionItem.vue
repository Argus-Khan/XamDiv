<template>
    <v-container class="pa-5 ma-0 h-100">
        <v-row class="pa-0 ma-0">
            <v-col class="v-col-11 offset-0 pt-4 pl-0">
                <h2>Question {{ QuestionNumber }}</h2>
                <p>{{ MarkList[num] }} Pts.</p>
            </v-col>
            <v-col align="center" class="v-col-1 offset-0">
                <v-btn variant="tonal" rounded @click="this.$emit('CloseQuestion')">
                    <v-icon>mdi-close</v-icon>
                </v-btn>
            </v-col>
            <v-divider class="border-opacity-100"></v-divider>
        </v-row>
        <v-row>
            <v-col>
                    {{ QuestionList[num] }}
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
                'Devise an algorithm to insert a node in a Binary Search Tree.',
                'Define tree traversal and list some of the algorithms to traverse a binary tree.',
                'Write an algorithm to find the maximum subarray sum for a given array. In other words, find the maximum sum that can be achieved by taking contiguous elements from a given array of integers.',
                'Define insertion sort and selection sort.',
                'Write an algorithm to reverse a string. For example, if my string is "uhsnamiH" then my result will be "Himanshu".'
            ],
            MarkList: [
                5, 10, 15, 20, 25
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