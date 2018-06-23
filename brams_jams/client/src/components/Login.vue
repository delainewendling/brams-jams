<template>
    <div> Redirecting to Login Page... </div>
</template>

<script>
    export default {
        created: function() {
            window.location.href = "http://localhost:8000/login/";
        }
    }
</script>