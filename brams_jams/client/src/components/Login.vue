<template>
    <div> Redirecting to Login Page... </div>
</template>

<script>
import { mapGetters } from 'vuex';
    export default {
        computed: {
            ...mapGetters([
                'api_host_url',
            ])
        },
        created: function() {
            window.location.href = `${this.api_host_url}/login/`;
        }
    }
</script>