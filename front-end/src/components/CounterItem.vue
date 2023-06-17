<template>
    <div class="text-center">
        <v-chip variant="tonal" size="large" class="ml-13 text-center">
            {{ hours_string }} : {{ minutes_string }} : {{ seconds_string }}
        </v-chip>
    </div>
</template>
 
<script>
     export default {
         data () {
             return {
                 countDown: 7200,
                 seconds: 0,
                 minutes: 0,
                 hours: 2,
                 seconds_string: '00',
                 minutes_string: '00',
                 hours_string: '02'
             }
         },
         props: ['StartCountdown'],
         methods: {
             countDownTimer () {
                 if (this.countDown > 0) {
                    setTimeout(() => {
                        this.countDown -= 1
                        this.countDownTimer()
                        this.seconds = this.countDown % 60
                        this.minutes = ((this.countDown - this.seconds) / 60) % 60
                        this.hours = ((this.countDown - (this.minutes * 60) - this.seconds) / 3600)
                        this.hours_string = this.hours.toString().padStart(2, '0')
                        this.minutes_string = this.minutes.toString().padStart(2, '0')
                        this.seconds_string = this.seconds.toString().padStart(2, '0')
                     }, 1000)
                 }
             }
         },
         watch: {
            StartCountdown: function() {
                this.countDownTimer()
                }  
        },
     }
</script>