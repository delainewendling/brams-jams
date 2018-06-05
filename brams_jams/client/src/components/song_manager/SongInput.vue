<template>
    <div>
        <label for="new-song"> What's the song called? </label>
        <input id="new-song" v-model="song_title"></input>
        <button @click="saveSong()"> Save </button>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                song_title: ""
            }
        },
        methods: {
            saveSong(){
                this.$emit("saveSong", this.song_title)
            }
        }
    }
</script>