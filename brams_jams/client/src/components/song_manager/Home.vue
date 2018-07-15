<template>
  <div class="container">
    <tags-input
        element-id="tag"
        v-model="selected_tags"
        :placeholder="'Search songs by tags'"
        :existing-tags="existing_tags"
        :typeahead="true"
        :disabled="selected_tags.length == 0 ? true : false">
    </tags-input>
    <song-list
        :songs="visible_songs"
        :searching="selected_tags.length > 0"
        :existing_tags="existing_tags"
        @songDeleted="songDeleted"
        class="song-list">
    </song-list>
    <div>
        <button
            @click="newSong()"
            v-show="!create_song"
            class="button add-song-btn">
            Add Song
        </button>
    </div>
    <song-input-panel
        @saveSong="saveSong"
        class="song-input-panel"
        :autocompleteItems="existing_tags"
        :create_song="create_song">
    </song-input-panel>
  </div>
</template>

<script>
import SongInputPanel from './SongInputPanel.vue';
import SongList from './SongList.vue';
import VueTagsInput from '@johmun/vue-tags-input';
import {axiosHelpers} from '../../helpers/axiosHelpers.js';
export default {
    data() {
        return {
            create_song: false,
            songs: [],
            search_tags: [],
            visible_songs: [],
            selected_tags: [],
            existing_tags: {},
            tag: ''
        }
    },
    watch: {
        selected_tags () {
            let search_tags = this.selected_tags;
            if (search_tags) {
                this.visible_songs = this.songs.filter((song)=> {
                    let matches_tag = false;
                    let song_tags = [];
                    song.song_tags.forEach((song_tag) => {
                        song_tags = [...song_tags, song_tag.tag.name]
                    });
                    matches_tag = search_tags.every((tag) => {
                        if (song_tags.includes(tag)) {
                            return tag
                        }
                    });
                    if (matches_tag) {
                        return song
                    }
                });
            } else {
                this.visible_songs = this.songs
            }
        }
    },
    components: {SongInputPanel, SongList, VueTagsInput},
    created() {
        axiosHelpers.getRequest('http://localhost:8000/song_manager/songs')
        .then(response => {
            this.$store.dispatch('setMessage',
                '','');
            console.log("songs ", response.data)
            this.songs = response.data;
            this.visible_songs = response.data;
        })
        .catch(error => {
            // TODO: make a class of types
            this.$store.dispatch('setMessage',
                'There was an error getting your songs. Refresh the page and try again',
                'error')
        });
        axiosHelpers.getRequest('http://localhost:8000/song_manager/tags')
        .then(response => {
            this.$store.dispatch('setMessage',
                '','')
            console.log("tags ", response.data)
            response.data.forEach((tag, index) => {
                this.existing_tags[tag.name] = tag.name;
            });
        })
        .catch(error => {
            // TODO: make a class of types
            this.$store.dispatch('setMessage',
                'There was an error getting your tags. Refresh the page and try again',
                'error')
            console.log("error ", error)
        })
    },
    methods: {
        saveSong(song_details){
            let song_title = song_details.song_title;
            if (!(song_title.replace(" ", ""))){
                this.$store.dispatch('setMessage',
                    'You need to fill in the song title before saving',
                    'error')
            } else {
                this.$store.dispatch('setMessage', '', '');
                axiosHelpers.postRequest('http://localhost:8000/song_manager/songs', song_details)
                .then(response => {
                    this.$store.dispatch('setMessage', '', '');
                    this.songs = [response.data, ...this.songs]
                    this.visible_songs = [response.data, ...this.songs]
                    //TODO: Make sure new tags are added here
                    this.create_song = false;
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
        },
        songDeleted(songId) {
            this.songs = this.songs.filter(song => song.id != songId)
            this.visible_songs = this.visible_songs.filter(song => song.id != songId)
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.new-tag-input::-webkit-input-placeholder::before {
    content:"Search songs by tag";
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
