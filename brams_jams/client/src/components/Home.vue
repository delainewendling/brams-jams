<template>
  <div>
    <button @click="newSong()" v-show="!create_song"> New Song </button>
    <song-input @saveSong="saveSong" v-show="create_song"></song-input>
    <song-list :songs="songs"></song-list>
  </div>
</template>

<script>
import SongInput from './song_manager/SongInput.vue';
import SongList from './song_manager/SongList.vue';
export default {
    data() {
        return {
            create_song: false,
            songs: [
                {
                    title: "Take Me Home"
                }
            ]
        }
    },
    components: {SongInput, SongList},
    methods: {
        saveSong(song_title){
            console.log("what's the song title? ", song_title)
        },
        newSong(){
            this.create_song = !this.create_song;
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
