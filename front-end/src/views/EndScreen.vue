<template>
    <div class=" h-100 bg-blue-grey-darken-3">
        <div class="center">
            <h1>End of demo</h1>
            <p>Thank you for your attention!</p>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'EndScreen',
  
    components: {
    },

    data() {
        return {
        }
    },

    methods: {
    }
});
</script>

<style scoped>
.center {
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
h1 {
    font-size: 80px;
    text-align: center;
    font-family: Roboto Mono;
}
p {
    font-size: 30px;
    text-align: center;
    font-family: Roboto Mono;
}
</style>