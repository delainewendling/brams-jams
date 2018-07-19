<template>
    <div>
        <div class="song-list" v-if="songs.length > 0">
            <div v-for="song in songs" class="song-item-container">
                <div class="song-item">
                    <div class="text">
                        <span class="song-name"> {{song.name}} </span>
                        <span class="num-tags" v-if="song.song_tags.length > 0"> {{song.song_tags.length}} tags </span>
                    </div>
                    <i class="material-icons md-18" v-show="!song.edit" @click="toggleSong(song)">keyboard_arrow_down</i>
                    <i class="material-icons md-18" v-show="song.edit" @click="toggleSong(song)">keyboard_arrow_up</i>
                    <i class="material-icons md-18 delete-btn" @click="openDeleteModal(song.id, song.name)">delete</i>
                </div>
                <div class="song-tags" v-show="song.edit">
                    <tags-input
                        element-id="tag"
                        :value="song.song_tags"
                        @input="updateTags(song, $event)"
                        :placeholder="'Add tags'"
                        :existing-tags="existing_tags"
                        :typeahead="true">
                    </tags-input>
                </div>
            </div>
        </div>
        <modal v-if="showModal" @close="showModal = false" @submit="deleteSong()">
            <h3 slot="body">Are you sure you want to delete {{songToDelete}}? </h3>
        </modal>
        <div class="no-songs-for-search" v-if="songs.length == 0 && searching">
            <p> There are no songs for this set of tags. Change or clear the search and try again. </p>
        </div>
        <div class="no-songs-for-search" v-if="songs.length == 0 && !searching">
            <p> You haven't added any songs yet. </p>
        </div>
    </div>
</template>

<script>
import Modal from '../common/Modal.vue';
import { axiosHelpers } from '../../helpers/axiosHelpers.js';
export default {
    data(){
        return {
            showModal: false,
            songIdToDelete: 0,
            songToDelete: '',
            tag: ''
        }
    },
    props: ['songs', 'searching', 'existing_tags'],
    components: {Modal},
    methods: {
        toggleSong(song){
            song.edit = !song.edit;
        },
        openDeleteModal(songId, songName) {
            this.songIdToDelete = songId;
            this.songToDelete = songName;
            this.showModal = true;
        },
        deleteSong() {
            this.$store.dispatch('setMessage','','');
            axiosHelpers.deleteRequest(`http://localhost:8000/song_manager/songs/${this.songIdToDelete}`)
            .then((response) => {
                console.log("what is the response? ", response)
                this.$emit('songDeleted', this.songIdToDelete)
                this.showModal = false;
            })
            .catch((err) => {
                this.$store.dispatch('setMessage',
                    'There was an error deleting that song. Refresh the page and try again',
                    'error');
                console.log("error ", err)
            })
        },
        updateTags(song, current_song_tags){
            console.log("num song tags ", song.song_tags.length, " song tags ", song.song_tags)
            this.$store.dispatch('setMessage','','');
            let old_song_tags = song.song_tags
            if (current_song_tags.length > old_song_tags.length){
                // Add a song tag
                let new_tag = current_song_tags.filter(tag => !old_song_tags.includes(tag))[0]
                axiosHelpers.patchRequest(`http://localhost:8000/song_manager/songs/${song.id}`,
                    {
                        'add': true,
                        'tag_name': new_tag
                    })
                .then(response => {
                    song.song_tags = [...song.song_tags, new_tag]
                })
                .catch(err => {
                    this.$store.dispatch('setMessage',
                    'There was an error adding that tag. Refresh the page and try again',
                    'error')
                    console.log("error ", err)
                })
            } else if (current_song_tags.length < old_song_tags.length) {
                // Delete song tag
                let tag_to_delete = old_song_tags.filter(tag => !current_song_tags.includes(tag))[0]
                axiosHelpers.patchRequest(`http://localhost:8000/song_manager/songs/${song.id}`,
                    {
                        'add': false,
                        'tag_name': tag_to_delete
                    })
                .then(response => {
                    console.log("response ", response);
                    song.song_tags = song.song_tags.filter(song_tag => song_tag != tag_to_delete)
                })
                .catch(err => {
                    this.$store.dispatch('setMessage',
                    'There was an error deleting that tag. Refresh the page and try again',
                    'error');
                    console.log("error ", err);
                })
            }
        }
    }
}
</script>

<style scoped>
    .material-icons{
        cursor: pointer;
    }
    .song-list {
        margin-top: 25px;
    }
    .song-item {
        padding: 5px;
        display: flex;
    }
    .text {
        flex-grow: 2;
        text-align: left;
    }
    .song-name {
        display: inline-block;
        margin-right: 15px;
    }
    .song-tags {
        display: block;
    }
    .num-tags {
        font-size: 12px;
        color: #A71D17;
    }
    .md-18 {
        margin: 0 3px;
        color: #777;
        font-size: 18px;
    }
    .delete-btn:hover {
        color: #bbb;
    }
    .song-item-container {
        padding: 5px;
        margin: 5px;
        box-shadow: 0px 0.5px 1px rgba(0,0,0,0.2);
    }
    span.badge-light {
        background-color: #aaa;
        border-radius: 5px;
    }
</style>