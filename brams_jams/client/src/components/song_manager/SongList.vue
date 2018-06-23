<template>
    <div>
        <div class="song-list-container" v-if="songs.length > 0">
            <h4 class="song-header"> Songs </h4>
            <div v-for="song in songs" class="song-item">
                <div> {{song.name}} </div>
                <i class="material-icons">edit</i>
                <i class="material-icons">close</i>
            </div>
        </div>
        <div class="no-songs-for-search" v-else>
            <p> There are no songs for this set of tags. Change the search and try again. </p>
        </div>
    </div>
</template>

<script>
export default {
    props: ['songs']
}
</script>

<style>
    .song-header {

    }
    .song-item {
        display: flex;
    }
</style>