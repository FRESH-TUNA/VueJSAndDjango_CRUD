<template>
    <div>
        <div v-for="element in posts" :element="element" :key="element.id" class="postStyleObject">
            <div class="postTitleStyleObject">
            <h3>{{element.title}}</h3>
            <a>{{element.published_date}}</a>
            </div>
            <div>{{element.content}}</div>
            <div class="postButtonsStyleObject">
            <button class="btn btn-primary" @click="onClickUpdate(element.id)">update</button>
            <button class="btn btn-primary" @click="deletePost(element.id)">delete</button>
            </div>
        </div>
    </div>
</template>

<script>
module.exports = {
    data: function() {
        return {
            posts: ''
        }
    },
    methods: {
        onClickUpdate (id) {
            axios.get('http://127.0.0.1:8000/AuthAPI/' + id + '/checkAuthToPost')
                .then(response => {
                    if (response.data.result === 'true') {
                        this.$emit('on-click-update', id)
                    }
                }
            );
        },
        checkAuthToPost(id) {
            axios.get('http://127.0.0.1:8000/AuthAPI/' + id + '/checkAuthToPost')
                .then(response => {
                    if (response.data.result === 'true') {
                        return true;
                    }
                }
            );
        },
        deletePost(id) {
            checkAuthToPost(id).then(result => {
                if(result === true) {
                    axios.post('http://127.0.0.1:8000/api/' + id + '/delete',
                        {
                            headers: {X_CSRFTOKEN: this.csrftoken}, 
                        }).then(response => (this.readPosts()));
                    }
                }
            );
        },
        readPosts: function() {
            axios.get('http://127.0.0.1:8000/api/')
            .then(response => {
                this.posts = response.data.posts
            });
        },
    },
    created() {
        this.readPosts()
    } 
}
</script>

<style scoped>
postStyleObject {
    width: 100%;
    border: 1px solid black;
    margin-top: 10px;
}
postTitleStyleObject {
    display: flex;
    justify-content: space-between;
}
postButtonsStyleObject {
    display: flex;
    flex-direction: row-reverse;
}
</style>