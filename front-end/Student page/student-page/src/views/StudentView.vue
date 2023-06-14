<template>
    <StudentPage />
</template>
  
<script>
import { defineComponent } from 'vue';
  
// Components
import StudentPage from '../components/StudentPage.vue';

export default defineComponent({
    name: 'StudentPageView',
  
    components: {
        StudentPage,
    },
});
</script>
  