axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

Vue.config.productionTip = false
Vue.prototype.$eventBus = new Vue()

navApp = httpVueLoader('/static/js/navApp.vue')
contentApp = httpVueLoader('/static/js/contentApp.vue')
footerApp = httpVueLoader('/static/js/footerApp.vue')

new Vue({
    render: h => h(navApp),
}).$mount('#navApp')

new Vue({
    render: h => h(contentApp),
}).$mount('#contentApp')

new Vue({
    render: h => h(footerApp),
}).$mount('#footerApp')

