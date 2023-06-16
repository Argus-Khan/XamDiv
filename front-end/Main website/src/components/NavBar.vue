<template>
    <v-navigation-drawer expand-on-hover rail>
        
      <v-list>
          <v-list-item prepend-avatar="./student_icon.jpg" title="Ron Ismaili" subtitle="130050">
          </v-list-item>
        </v-list>
        
        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-help" title="Question 1" value="Question_1" @click="this.$emit('ChangeQuestion', 1)"></v-list-item>
          <v-list-item prepend-icon="mdi-help" title="Question 2" value="Question_2" @click="this.$emit('ChangeQuestion', 2)"></v-list-item>
          <v-list-item prepend-icon="mdi-help" title="Question 3" value="Question_3" @click="this.$emit('ChangeQuestion', 3)"></v-list-item>
          <v-list-item prepend-icon="mdi-help" title="Question 4" value="Question_4" @click="this.$emit('ChangeQuestion', 4)"></v-list-item>
          <v-list-item prepend-icon="mdi-help" title="Question 5" value="Question_5" @click="this.$emit('ChangeQuestion', 5)"></v-list-item>
          <v-divider></v-divider>
        </v-list>

      </v-navigation-drawer>
</template>