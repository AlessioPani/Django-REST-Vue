var app = new Vue( {
    el: '#app',
    data: {
        comment: null,
        comments: [],
        errors: null
    },
    methods: {
        onSubmit() {
            if (this.comment) {
                this.comments.push(this.comment);
                this.comment = null;

                if (this.errors) {
                    this.errors = null;
                }
            } else {
                this.errors ='Comment area must not be empty!'
            }
        }
    }
})