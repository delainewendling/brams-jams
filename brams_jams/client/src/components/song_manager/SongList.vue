<template>
    <div>
        <h4 class="song-header"> Songs </h4>
        <div v-for="song in songs" class="song-item">
            <div> {{song.title}} </div>
            <i class="material-icons">edit</i>
            <i class="material-icons">close</i>
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