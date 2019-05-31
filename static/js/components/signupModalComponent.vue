<template>    
    <div id="signupModal" @click="$emit('on-click-outside')">
        <div id="signupModalContent" @click.stop>
            <h1>Sign up!</h1>
            <form action="signup" method="POST">
                <label for="fname">e-mail</label>
                <input type="text" v-model="username">
                <label for="fname">password</label>
                <input type="password" v-model="password1">
                <label for="fname">repeat your password</label>
                <input type="password" v-model="password2">
                <button type="button"  @click="signup">회원가입</button>
            </form>
        </div>
    </div>
</template>    

<script>
module.exports = {
    data: function(){
        return {
            csrftoken: '',
            username: '',
            password1: '',
            password2: '',
        }
    },
    methods: {
        signup() {
            axios.post('http://127.0.0.1:8000/AuthAPI/signup', 
            {
                headers: {X_CSRFTOKEN: this.csrftoken}, 
                username : this.username, 
                password1: this.password1,
                password2: this.password2,
            }).then(response => {
                this.$emit('after-create-account')
            })
        }
    },
    created() {
            axios.get('http://127.0.0.1:8000/api/getCsrf')
                .then(response => (this.csrftoken = response.csrfToken)
            );
    }
}
</script>

<style scoped>
#signupModal {
    position: fixed;
    left: 0; 
    top: 0; 

    display: flex;
    align-content: center;
    align-items: center;
    justify-content: center;

    width: 100%;
    height: 100%;

    background-color: rgba(0, 0, 0, 0.5);
}

#signupModalContent {
    border: 3px solid rgb(167, 167, 167);
    border-radius: 10px;
    width: 400px;
    padding: 10px;

    background-color: rgb(230, 228, 228);
    z-index: 5;
}

input {
    width: 100%; 
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
    border: 3px solid #ccc;
    -webkit-transition: 0.5s;
    transition: 0.5s;
    outline: none;
}

input:focus {
    border: 3px solid #555;
}
</style>