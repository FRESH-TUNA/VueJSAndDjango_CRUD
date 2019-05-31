<template>
    <div id="mainView">
        <component 
            v-bind:is="currentComponent" 

            @on-click-update="showUpdatePostComponent"
            :post-pk-for-update="postPk"

            @after-create-post="showReadPostsComponent"
            @after-update-post="showReadPostsComponent"
        ></component>
    </div>
</template>

<script>
readPostsComponent = httpVueLoader('/static/js/components/readPostsComponent.vue')
createPostComponent = httpVueLoader('/static/js/components/createPostComponent.vue')
updatePostComponent = httpVueLoader('/static/js/components/updatePostComponent.vue')

module.exports = {
    data: function(){
        return {
            currentComponent: 'read-posts-component',
            postPk: [],
            csrftoken: ''
        }
    },
    components: {
        'read-posts-component':readPostsComponent,
        'create-post-component':createPostComponent,
        'update-post-component':updatePostComponent,
    },
    methods: {
        showReadPostsComponent: function() {
            this.currentComponent = 'read-posts-component'
        },
        showCreatePostComponent: function() {
            this.currentComponent = 'create-post-component'
        },
        showUpdatePostComponent: function(id) {
            this.postPk = id;
            this.currentComponent = 'update-post-component'
        }
    },
    created() {
        axios.get('http://127.0.0.1:8000/api/getCsrf')
            .then(response => (this.csrftoken = response.csrfToken)
        );
    },
    mounted() {
        this.$eventBus.$on('show-create-post-component', () => {
            this.showCreatePostComponent();
        }),
        this.$eventBus.$on('show-read-posts-component', () => {
            this.showReadPostsComponent();
        })
    }
}
</script>

<style>
#mainView {
    padding: 20px;
}
</style>
