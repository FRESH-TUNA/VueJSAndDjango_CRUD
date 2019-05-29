<template>
    <form>
        <div class="form-group">
            <label for="title">Title</label>
            <input type="text" class="form-control" placeholder="Enter title" v-model="post.title">
        </div>
        <div class="form-group">
            <label for="content">Content</label>
            <textarea class="form-control" v-model="post.content"></textarea>
        </div>
        <button type="button" class="btn btn-primary" @click="updatePost(post.id)">Submit</button>
    </form>
</template>

<script>
module.exports = {
    props: ['post-pk-for-update'],
    data: function() {
        return {
            post: '',
            csrftoken: ''
        }
    },
    methods: {
        updatePost(id) {
            axios.post('http://127.0.0.1:8000/api/' + id + '/update', 
            {
                headers: {X_CSRFTOKEN: this.csrftoken}, 
                title : this.post.title, 
                content: this.post.content
            }).then(() => {
                this.$emit('after-update-post')
            })
        }
    },
    created() {
        axios.get('http://127.0.0.1:8000/api/' + this.postPkForUpdate)
                .then(response => (this.post = response.data.post)
        );
        axios.get('http://127.0.0.1:8000/api/getCsrf')
            .then(response => (this.csrftoken = response.csrfToken)
        );
    }
}
</script>

<style scoped>
textarea {
    height: 300px;
}
</style>
