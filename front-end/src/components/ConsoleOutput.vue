<template>
    <v-container fluid class="pa-2 ma-0 temp">
        {{ Error }}
    </v-container>
</template>

<script>
export default {
    props:['Error']
}
</script>

<style scoped>
    .temp {
        color: #04ff00;
        overflow-y: auto;
        max-height: 19.9vh;
        background-color: #0d0f17;
        border-top: 5px solid #424242;
    }
</style>