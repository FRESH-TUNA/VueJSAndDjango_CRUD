<template>
    <nav class="navbar navbar-expand-lg navbar-light">
            <a class="navbar-brand" @click="showReadPostsComponent">{{title}}</a>
            <button type="button" class="btn btn-primary" @click="showCreatePostComponent">New Document</button>
    </nav>
</template>

<script>
module.exports = {
    data: function(){
        return {
            title: 'TunaBoard'
        }  
    },
    methods: {
        showCreatePostComponent() {
            this.$eventBus.$emit('show-create-post-component')
        },
        showReadPostsComponent() {
            this.$eventBus.$emit('show-read-posts-component')
        }
    }
}
</script>

<style scoped>
#nav {
    background-color: aliceblue;
}
</style>