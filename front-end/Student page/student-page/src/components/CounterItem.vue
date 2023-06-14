<template>
    <v-chip variant="elevated" class="timer">
        {{ countDown }}
    </v-chip>
</template>
 
<script>
     export default {
         data () {
             return {
                 countDown: 1000
             }
         },
         methods: {
             countDownTimer () {
                 if (this.countDown > 0) {
                     setTimeout(() => {
                         this.countDown -= 1
                         this.countDownTimer()
                     }, 1000)
                 }
             }
         },
         created () {
             this.countDownTimer()
         }
     }
</script>