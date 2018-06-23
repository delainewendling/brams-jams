<template>
  <div class="container">
    <vue-tags-input
      v-model="tag"
      :autocomplete-items="tags"
      :placeholder="'Search songs by tags'"
      @before-adding-tag="beforeAdd"
      @before-deleting-tag="beforeDelete"
      @tags-changed="newTags => tags = newTags"
    />
    <song-list
        :songs="visible_songs"
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
        :autocompleteItems="tags"
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
            tags: [],
            tag: ''
        }
    },
    components: {SongInputPanel, SongList, VueTagsInput},
    created() {
        axiosHelpers.getRequest('http://localhost:8000/song_manager/songs')
        .then(response => {
            console.log("response ", response)
            this.$store.dispatch('setMessage',
                '','');
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
            this.tags = response.data.map((tag) => {
                return {'text': tag.name}
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
            let song_title = song_details.song_title,
                tags = song_details.tags
            if (!(song_title.replace(" ", ""))){
                this.$store.dispatch('setMessage',
                    'You need to fill in the song title before saving',
                    'error')
            } else {
                this.$store.dispatch('setMessage', '', '');
                axiosHelpers.postRequest('http://localhost:8000/song_manager/songs', song_details)
                .then(response => {
                    this.$store.dispatch('setMessage', '', '');
                    this.songs = [...this.songs, response.data]
                    //TODO: Make sure new tags are added here
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
        beforeDelete(obj){
            obj.deleteTag();
            let index = this.search_tags.indexOf(obj.tag.text);
            console.log("what is the index? ", index)
            this.search_tags.splice(index, 1)
            console.log("what are the search tags? ", this.search_tags)
            this.searchSongs(obj)
        },
        beforeAdd(obj){
            obj.addTag()
            this.search_tags = [...this.search_tags, obj.tag.text]
            this.searchSongs(obj)
        },
        searchSongs(obj){
            if (this.search_tags) {
                this.visible_songs = this.songs.filter((song)=> {
                    let matches_tag = false;
                    let song_tags = [];
                    song.song_tags.forEach((tag) => {
                        song_tags = [...song_tags, tag.tag.name]
                    });
//                    console.log("these are the search tags", this.search_tags, " these are the song tags? ", song_tags)
                    matches_tag =  this.search_tags.every((tag) => {
//                        console.log("this is the tag ", tag)
                        song_tags.includes(tag)
                    })
                    if (matches_tag) {
                        return song
                    }
                });
            } else {
                console.log("inside else")
                this.search_tags = this.search_tags.pop()
                this.visible_songs = this.songs
            }
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
