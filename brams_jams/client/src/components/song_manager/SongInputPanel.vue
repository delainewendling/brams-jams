<template>
    <div class="song-panel" v-if="create_song">
        <label for="new-song"> What's the song called? </label>
        <input
            ref="song_title"
            id="new-song"
            v-model="song_title"
            placeholder="Song title"
        />
        <tags-input
            element-id="tag"
            v-model="tags"
            :existing-tags="autocompleteItems"
            :typeahead="true"
            :deleteOnBackspace="false">
        </tags-input>
        <div class="song-btns">
            <button class="button is-small" @click="$emit('cancel')"> Cancel </button>
            <button class="button is-small" @click="saveSong()"> Save </button>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                song_title: '',
                tag:'',
                tags: [],
            }
        },
        props: ['create_song', 'autocompleteItems'],
        watch: {
            create_song() {
                if (this.create_song) {
                    console.log("refs ", this.$refs)
                    this.$refs.song_title.focus()
                }
            }
        },
        methods: {
            saveSong(){
                let song_details = {
                    'song_title': this.song_title,
                    'tags': this.tags
                };
                this.song_title = '';
                this.tags = [];
                this.$emit("saveSong", song_details);
            }
        }
    }
</script>

<style scoped>
    #new-song {
        padding: 3px;
        width: 100%;
        height: 33px;
        margin: 15px 0;
    }
    input,
    .tags-input,
    input::-webkit-input-placeholder {
        font-size: 14px;
        line-height: 3;
    }
    .song-btns {
        margin: 10px;
    }
    button {
        margin: 10px;
    }
</style>
