<template>    
<div id="signinModal" @click="$emit('on-click-outside')">
    <div id="signinModalContent" @click.stop>
        <h1>Sign in!</h1>
        <form action="signup" method="POST">
                <label for="fname">e-mail</label>
                <input type="text" v-model="username">
                <label for="fname">password</label>
                <input type="password" v-model="password">
                <button type="button" class="myButton" @click="signin">로그인</button>
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
            password: '',
        }
    },
    methods: {
        signin() {
            axios.post('http://127.0.0.1:8000/AuthAPI/signin', 
            {
                headers: {X_CSRFTOKEN: this.csrftoken}, 
                username : this.username, 
                password: this.password
            }).then(response => {
                // if(response.data.result === 'success')
                    this.$emit('after-login-success', this.username)
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
#signinModal {
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

#signinModalContent {
    border: 3px solid rgb(167, 167, 167);
    border-radius: 10px;
    width: 400px;
    padding: 10px;

    background-color: rgb(230, 228, 228);
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
