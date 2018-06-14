<template>
    <div class="song-panel" v-if="create_song">
        <label for="new-song"> What's the song called? </label>
        <input
            id="new-song"
            v-model="song_title"
            placeholder="Song title"
        ></input>
        <vue-tags-input
          v-model="tag"
          :tags="tags"
          :autocomplete-items="filteredItems"
          @tags-changed="newTags => tags = newTags"
        />
        <button @click="saveSong()"> Save </button>
    </div>
</template>

<script>
import VueTagsInput from '@johmun/vue-tags-input';
    export default {
        data() {
            return {
                song_title: "",
                tag: '',
                tags: [],
                autocompleteItems: [
                {
                    text: 'Male',
                },
                {
                    text: 'Thomas Rhett',
                }],

            }
        },
        components: {VueTagsInput},
        props: ['create_song'],
        computed: {
            filteredItems() {
                return this.autocompleteItems.filter(i => new RegExp(this.tag, 'i').test(i.text));
            },
        },
        methods: {
            saveSong(){
                this.$emit("saveSong", this.song_title)
            }
        }
    }
</script>

<style>
    .song-panel {
        width: 20%;
        z-index: 1000;
    }
    #new-song {
        height: 1.5rem;
    }
</style>