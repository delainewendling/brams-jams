<template>
    <div class="song-panel" v-if="create_song">
        <label for="new-song"> What's the song called? </label>
        <input
            id="new-song"
            v-model="song_title"
            placeholder="Song title"
        ></input>
        <div>
            <tags-input
                element-id="tag"
                v-model="tags"
                :existing-tags="autocompleteItems"
                :typeahead="true"
                :deleteOnBackspace="false">
            </tags-input>
        </div>
        <button @click="saveSong()"> Save </button>
    </div>
</template>

<script>
import VueTagsInput from '@johmun/vue-tags-input';
    export default {
        data() {
            return {
                song_title: '',
                tag:'',
                tags: [],
            }
        },
        components: {VueTagsInput},
        props: ['create_song', 'autocompleteItems'],
        computed: {
            filteredItems() {
                return this.autocompleteItems.filter(i => new RegExp(this.tag, 'i').test(i.text));
            },
        },
        methods: {
            saveSong(){
                let song_details = {
                    'song_title': this.song_title,
                    'tags': this.tags
                }
                this.song_title = ''
                this.tags = []
                this.$emit("saveSong", song_details)
            }
        }
    }
</script>

<style>

</style>

//<vue-tags-input
//          v-model="tag"
//          :tags="tags"
//          :autocomplete-items="filteredItems"
//          @tags-changed="newTags => tags = newTags"
//        />