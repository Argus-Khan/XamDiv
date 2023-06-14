<template>
  <v-container fluid style="background: url(/Login_Background.jpg); background-size: cover;" class="h-100 w-auto px-lg-16">
    <v-row align="center" class="h-100 mx-lg-16 px-lg-16">
      <v-col align="center" style="background-color: #512DA8CC" class="rounded-lg hidden-md-and-up">
        <p class="text-red font-weight-bold text-h3">This app is not meant to be used with small devices, please use a larger device.</p>
      </v-col>
      <v-col align="center" style="background-color: #512DA8CC" class="v-col-4 offset-4 rounded-xl h-50 hidden-sm-and-down pa-10">
        <p class="text-white text-h4">XamDiv Login</p>
        <v-form @submit.prevent="" class="py-8" style="height: 100%;">
          <v-text-field v-model="ID" label="User ID" class="text-white" color="white"></v-text-field>
          <v-text-field v-model="Password" label="Password" class="text-white" color="white" type="password" v-if="ProfID()"></v-text-field>
          <v-btn type="Submit" class="bg-deep-purple-darken-4 rounded-pill">Submit</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue';

// Components


export default defineComponent({
  name: 'HomeView',
  data() {
    return {
      ID:'',
      Pass: '',
    };
  },
  methods: {
    ProfID: function() {
      console.log(((this.ID.length > 9))? true: false);
      return ((this.ID.length > 9))? true: false;
    }
  }
});
</script>
