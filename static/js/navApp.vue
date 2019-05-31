<template>
    <nav class="navbar navbar-expand-lg navbar-light">
            <a class="navbar-brand" @click="showReadPostsComponent">{{title}}</a>
            <button type="button" class="btn btn-primary" @click="showCreatePostComponent" v-show="loginState">New Document</button>
            <button type="button" class="btn btn-primary" @click="signout" v-show="loginState">Sign out</button>
            <button type="button" class="btn btn-primary" @click="showSignInModal" v-show="!loginState">Sign in</button>
            <button type="button" class="btn btn-primary" @click="showSignupModal">Sign up</button>
        
            <component
                :is="modalComponentState"
                @on-click-outside="modalComponentState = false"
                
                @after-create-account="modalComponentState = false"
                @after-login-success="showUserInfo"
            ></component>
            <a class="navbar-brand" v-if="loginState">welcome {{username}}</a>
    </nav>
</template>

<script>
signupModalComponent = httpVueLoader('/static/js/components/signupModalComponent.vue')
signinModalComponent = httpVueLoader('/static/js/components/signinModalComponent.vue')

module.exports = {
    data: function(){
        return {
            title: 'TunaBoard',
            modalComponentState: null,
            loginState: false,
            username: ''
        }  
    },
    components: {
        'signupModalComponent':signupModalComponent,
        'signinModalComponent':signinModalComponent,
    },
    methods: {
        showCreatePostComponent() {
            if(this.loginState === true)
                this.$eventBus.$emit('show-create-post-component')
        },
        showReadPostsComponent() {
            this.$eventBus.$emit('show-read-posts-component')
        },
        showSignupModal() {
            this.modalComponentState = 'signupModalComponent'
        },
        showSignInModal() {
            this.modalComponentState = 'signinModalComponent'
        },
        closeModal() {
            this.modalComponentState = null
        },
        setLoginState() {
            this.loginState = !(this.loginState)
            console.log(this.loginState)
        },
        showUserInfo(username) {
            this.closeModal();
            this.username = username
            this.setLoginState()
        },
        signout() {
            axios.get('http://127.0.0.1:8000/AuthAPI/signout')
                .then(response => {
                    this.username = ''
                    this.setLoginState()
                })
        }
    },
    created() {
        axios.get('http://127.0.0.1:8000/AuthAPI/loginState')
            .then(response => {
                if(response.data.result !== 'false') {
                    this.username = response.data.result
                    this.setLoginState()
                }
            })
    }
}
</script>

<style scoped>
nav {
    height: 30px;
    background-color: aliceblue;
}
</style>