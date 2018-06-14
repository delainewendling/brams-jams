<template>
  <div class="song-manager-container">
    <song-list
        :songs="songs"
        class="song-list">
    </song-list>
    <div>
        <button
            @click="newSong()"
            v-show="!create_song"
            class="add-song-btn">
            Add Song
        </button>
    </div>
    <song-input-panel
        @saveSong="saveSong"
        class="song-input-panel"
        :create_song="create_song">
    </song-input-panel>
  </div>
</template>

<script>
import SongInputPanel from './SongInputPanel.vue';
import SongList from './SongList.vue';
import axios from 'axios';
export default {
    data() {
        return {
            create_song: false,
            songs: [
                {
                    title: "Take Me Home"
                }
            ],
        }
    },
    components: {SongInputPanel, SongList},
    created() {
        axios.get('http://localhost:8000/song_manager/songs')
        .then(response => {
            console.log("response ", response)
            this.$store.dispatch('setMessage',
                '','')
        })
        .catch(error => {
            // TODO: make a class of types
            this.$store.dispatch('setMessage',
                'There was an error getting your songs. Refresh the page and try again',
                'error')
            console.log("error ", error)
        })
    },
    methods: {
        saveSong(song_title){
            console.log("what's the song title? ", song_title)
            if (!(song_title.replace(" ", ""))){
                this.$store.dispatch('setMessage',
                    'You need to fill in the song title before saving',
                    'error')
            } else {
                this.$store.dispatch('setMessage', '', '');
                axios.post('http://localhost:8000/song_manager/songs', {name: song_title})
                .then(response => {
                    this.$store.dispatch('setMessage', '', '');
                    console.log("response ", response)
                })
                .catch(error => {
                    console.log("error ", error)
                    this.$store.dispatch('setMessage',
                    'There was an error saving your song. Refresh the page and try again.',
                    'error')
                })
            }
        },
        newSong(){
            this.create_song = !this.create_song;
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.song-manager-container {
    display: flex;
    justify-content: space-between;
}
.song-input-panel {
    align-self: flex-end;
}
.song-list {
    flex-grow: 1.5;
    background-color: white;
}
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
