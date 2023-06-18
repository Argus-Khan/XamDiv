<template>
    <v-container fluid class="pa-2 ma-0 temp">
        <p class="console-text-awaiting" v-if="this.Error === 'Awaiting first compile...'">{{ Error }}</p>
        <p class="console-text-success" v-if="this.Error === 'Successful Compile'">{{ Error }}</p> 
        <p class="console-text-error" v-if="this.Error !== 'Successful Compile' && this.Error !== 'Awaiting first compile...'">{{ Error }}</p>
</v-container>
</template>

<script>
export default {
    props:['Error']
}
</script>

<style scoped>
.temp {
    overflow-y: auto;
    max-height: 19.9vh;
    background-color: #0d0f17;
    border-top: 5px solid #424242;
}
.console-text-awaiting {
    color: white;
}
.console-text-success {
    color: #04ff00;
}
.console-text-error {
    color: red;
}
</style>