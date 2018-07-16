<template>
    <div>
        <div class="song-list-container" v-if="songs.length > 0">
            <h4 class="song-header"> Songs </h4>
            <div v-for="song in songs" class="song-item">
                <div> {{song.name}} </div>
                <i class="material-icons" v-show="!song.edit" @click="toggleSong(song)">keyboard_arrow_down</i>
                <i class="material-icons" v-show="song.edit" @click="toggleSong(song)">keyboard_arrow_up</i>
                <div v-show="song.edit">
                    <tags-input
                        element-id="tag"
                        :value="song.song_tags"
                        @input="updateTags(song, $event)"
                        :placeholder="'Add tags'"
                        :existing-tags="existing_tags"
                        :typeahead="true">
                    </tags-input>
                </div>
                <i class="material-icons" @click="openDeleteModal(song.id, song.name)">close</i>
            </div>
        </div>
        <modal v-if="showModal" @close="showModal = false" @submit="deleteSong()">
            <h3 slot="body">Are you sure you want to delete {{songToDelete}}? </h3>
        </modal>
        <div class="no-songs-for-search" v-if="songs.length == 0 && searching">
            <p> There are no songs for this set of tags. Change the search and try again. </p>
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
    .song-item {
        display: flex;
    }
</style>