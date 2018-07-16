<template>
    <div v-if="message.message">
        <i class="material-icons">{{icon}}</i>
        {{message.message}}
        <i class="material-icons" @click="close()">close</i>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    data() {
        return {
            icon: '',
        }
    },
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