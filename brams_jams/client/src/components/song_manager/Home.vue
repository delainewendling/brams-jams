<template>
    <div class="container">
        <div class="song-management-container">
            <div class="add-song-container">
                <button
                    @click="newSong()"
                    v-show="!create_song"
                    class="button add-song-btn">
                    Add Song
                </button>
                <song-input-panel
                    @saveSong="saveSong"
                    @cancel="cancelSong"
                    class="song-input-panel"
                    :autocompleteItems="existing_tags"
                    :create_song="create_song">
                </song-input-panel>
            </div>
            <div class="song-list-container">
                <div class="search-bar-container">
                    <div class="search-bar">
                        <tags-input
                            element-id="tag"
                            v-model="selected_tags"
                            :placeholder="'Search songs by tags'"
                            :existing-tags="existing_tags"
                            :typeahead="true">
                        </tags-input>
                    </div>
                    <div class="clear-icon">
                        <i class="material-icons md-18" @click="clearSearch()">clear</i>
                    </div>
                </div>
                <div class="song-list">
                    <song-list
                        :songs="visible_songs"
                        :searching="selected_tags.length > 0"
                        :existing_tags="existing_tags"
                        @songDeleted="songDeleted"
                        class="song-list">
                    </song-list>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import SongInputPanel from './SongInputPanel.vue';
import SongList from './SongList.vue';
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
                    let matches_tag = search_tags.every((tag) => {
                        if (song.song_tags.includes(tag)) {
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
    components: {SongInputPanel, SongList},
    created() {
        axiosHelpers.getRequest('http://localhost:8000/song_manager/songs')
        .then(response => {
            this.$store.dispatch('setMessage',
                '','');
            let songs = response.data.map(song => {
                return this.reformatSongs(song)
            });
            this.songs = songs;
            this.visible_songs = songs;
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
        reformatSongs(song){
            let song_tags = [];
            song.song_tags.forEach((song_tag) => {
                song_tags = [...song_tags, song_tag.tag.name]
            });
            song.edit = false;
            song.song_tags = song_tags;
            return song
        },
        cancelSong(){
            this.create_song = false;
        },
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
                    let song = this.reformatSongs(response.data);
                    this.songs = [song, ...this.songs];
                    this.visible_songs = [song, ...this.visible_songs];
                    //TODO: Make sure new tags are added here
                    this.create_song = false;
                })
                .catch(error => {
                    console.log("error ", error);
                    this.$store.dispatch('setMessage',
                    'There was an error saving your song. Refresh the page and try again.',
                    'error');
                })
            }
        },
        newSong(){
            this.create_song = !this.create_song;
        },
        songDeleted(songId) {
            this.songs = this.songs.filter(song => song.id !== songId);
            this.visible_songs = this.visible_songs.filter(song => song.id !== songId);
        },
        clearSearch(){
            this.selected_tags = [];
            this.visible_songs = this.songs;
        }
    }
}
</script>

<style scoped>
    .search-bar-container {
        display: flex;
        position: fixed;
        background-color: white;
        padding-bottom: 15px;
        width: 62%;
    }
    .search-bar {
        flex-grow: 2;
    }
    .add-song-btn {
        background-color: #0080FF;
        color: white;
        border-color: white;
    }
    .add-song-btn:hover {
        background-color: #10A0FF;
        color: white;
        border-color: white;
    }
    .song-management-container {
        display: flex;
        justify-content: space-between;
        margin-top: 20px;
    }
    .song-list-container {
        flex-basis: 70%;
        padding: 20px;
        border: solid 0.5px #ddd;
        max-height: 88vh;
        overflow: auto;
    }
    .song-list {
        margin-top: 55px;
    }
    .add-song-container {
        flex-basis: 27%;
        padding: 18px;
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
    .tags-input input {
        font-size: 12px;
    }
    .md-18 {
        cursor: pointer;
        font-size: 18px;
        margin: 8px;
    }
</style>
