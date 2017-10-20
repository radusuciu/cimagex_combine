Vue.use(VueResource);

var app = new Vue({
    el: '#app',
    data: {

    },
    computed: {

    },
    methods: {
        process: function() {
            this.$http.get('/api/combine').then(function(response) {
                console.log(response);
            });
        }
    }
});
