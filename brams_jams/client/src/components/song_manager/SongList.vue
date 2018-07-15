<template>
    <div>
        <div class="song-list-container" v-if="songs.length > 0">
            <h4 class="song-header"> Songs </h4>
            <div v-for="song in songs" class="song-item">
                <div> {{song.name}} </div>
                <i class="material-icons" v-show="!song.edit" @click="toggleSong(song)">keyboard_arrow_down</i>
                <i class="material-icons" v-show="song.edit" @click="toggleSong(song)">keyboard_arrow_up</i>
                <div v-show="!song.edit">
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
            console.log("clicked! ", song)
            song.edit = !song.edit
        },
        openDeleteModal(songId, songName) {
            this.songIdToDelete = songId;
            this.songToDelete = songName;
            this.showModal = true;
        },
        deleteSong() {
            axiosHelpers.deleteRequest(`http://localhost:8000/song_manager/songs/${this.songIdToDelete}`)
            .then((response) => {
                console.log("what is the response? ", response)
                this.$emit('songDeleted', this.songIdToDelete)
                this.showModal = false;
            })
            .catch((err) => {
                console.log("error ", err)
            })
        },
        getSongTags(songTags){
            console.log("song tags ", songTags)
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