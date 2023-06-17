<template>
  <v-container fluid class="h-100 w-auto px-lg-16 Background">
    <v-row align="center" class="h-100 mx-lg-16 px-lg-16">
      <v-col align="center" class="rounded-lg hidden-md-and-up">
        <p class="text-red font-weight-bold text-h3">This app is not meant to be used with small devices, please use a larger device.</p>
      </v-col>
      <v-col align="center" class="v-col-4 offset-4 rounded-xl h-50 hidden-sm-and-down pa-10">
        <p class="text-white text-h4">XamDiv Login</p>
        <v-form @submit.prevent="SendToExam" class="py-8 h-100">
          <v-btn-toggle class="w-100 mb-8" v-model="UserType" mandatory>
              <v-btn text class="text-white rounded-pill mx-4" style="width: 40%; height: 100%;" value="Student">Student</v-btn>
              <v-btn text class="text-white rounded-pill mx-6" style="width: 40%; height: 100%;" value="Professor">Professor</v-btn>
          </v-btn-toggle>
          <v-text-field v-model="ID" type="text" label="User ID" class="text-white" color="white">
            <template v-slot:prepend>
              <v-icon class="rounded-circle" icon="mdi-school" size="x-large"></v-icon>
            </template>
          </v-text-field>
          <v-text-field v-model="ExamId" label="Exam ID" class="text-white" color="white" type="text" v-if="UserType === 'Student'">
            <template v-slot:prepend>
              <v-icon class="rounded-circle" icon="mdi-pound" size="x-large"></v-icon>
            </template>
          </v-text-field>
          <v-text-field v-model="Password" label="Password" class="text-white" color="white" type="password" v-if="UserType === 'Professor'">
            <template v-slot:prepend>
              <v-icon class="rounded-circle" icon="mdi-lock" size="x-large"></v-icon>
            </template>
          </v-text-field>
          <v-btn type="Submit" elevation="8" class="rounded-pill text-lowercase text-white">login</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue';
import { aliases, mdi } from 'vuetify/iconsets/mdi'

// Components


export default defineComponent({
  name: 'HomeView',
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
  data() {
    return {
      ExamId: '',
      ID:'',
      Pass: '',
      UserType: 'Student',
      Password: ''
    };
  },
  methods: {
    SendToExam: function() {
      this.$router.push('/Student');
    }
  }
});
</script>

<style scoped>
  .v-container.Background {
    font-family: Roboto Mono;
    background: url(../assets/Login_Background.jpg);
    background-size: cover;
  }
  .v-col {
    background-color: #A08FFFF2;
  }
  .v-btn {
    background-color: #6B67C6;
    width: 25%;
  }
  .v-icon {
    width: 50px;
    height: 50px;
    color: white;
    background-color: #6B67C6;
  }
</style>