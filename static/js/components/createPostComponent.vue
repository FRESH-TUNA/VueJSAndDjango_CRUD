<template>
    <form>
        <div class="form-group">
            <label for="title">Title</label>
            <input type="text" class="form-control" placeholder="Enter title" v-model="title">
        </div>
        <div class="form-group">
            <label for="content">Content</label>
            <textarea class="form-control" v-model="content"></textarea>
        </div>
        <button type="button" class="btn btn-primary" @click="createPost">Submit</button>
    </form>
</template>

<script>
module.exports = {
    props: ['currentViewData'],
    data: function() {
        return {
            title: '',
            content: '',
            csrftoken: ''
        }
    },
    methods: {
        createPost: function() {
            axios.post('http://127.0.0.1:8000/api/create', 
            {
                headers: {X_CSRFTOKEN: this.csrftoken}, 
                title : this.title, 
                content: this.content
            }).then(response => {
                this.$emit('after-create-post')
            })
        },
        created() {
            axios.get('http://127.0.0.1:8000/api/getCsrf')
                .then(response => (this.csrftoken = response.csrfToken)
            );
        }
    }
}
</script>

<style scoped>
textarea {
    height: 300px;
}
</style>
