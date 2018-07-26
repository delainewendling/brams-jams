<template>
    <div v-if="message.message" class="message-container">
            <strong class="error"> Error: </strong>  {{message.message}}
        <i class="material-icons md-18" @click="close()">close</i>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    computed: {
        ...mapGetters([
           'message',
           'type'
        ])
    },
    methods: {
        close() {
            this.$store.dispatch('setMessage', '', '')
        }
    }
}
</script>

// This is the red we want - convert to decimal: F2DEDE
<style scoped>
    .message-container {
        display: flex;
        justify-content: center;
        margin: 10px 15%;
        padding: 8px;
        background-color: rgba(255, 0, 0, 0.2);
        border: solid 0.5px rgba(255, 0, 0, 0.3);
        border-radius: 5px;
        color: #A74544;
    }
    .error {
        color: #A74544;
    }
    .md-18 {
        cursor: pointer;
        font-size: 18px;
        margin: 4px 0 4px 8px;
    }
</style>