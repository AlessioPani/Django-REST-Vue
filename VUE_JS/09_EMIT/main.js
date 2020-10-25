// Comment list component
Vue.component('comment-list', {

    props: {
        comments: {
            type: Array,
            required: true
        }
    },
    data: function() {
        return {
            new_comment: null,
            comment_author: null,
            error: null
        }
    },

    methods: {
        submitComment() {
            if (this.comment_author && this.new_comment) 
            {
                this.$emit('submit-comment', {username: this.comment_author, 
                                              content: this.new_comment});
                this.comment_author = null;
                this.new_comment = null;

                if (this.error) 
                {
                    this.error = null;
                }
            } else {
                this.error = 'Fill all the fields!'
            }
        }
    },

    template: `
    <div class="mt-2">
        <div class="container">
            <single-comment
                            v-for="(comment, index) in comments"
                            :comment="comment"
                            :key="index"
            ></single-comment>
            <hr>
            <h3>{{ error }}</h3>

            <form @submit.prevent="submitComment">
                <div class="form-group">
                    <label for="comment_author">Your name</label>
                    <input id="comment_author" 
                    class="form-control"     
                    type="text" 
                    v-model="comment_author"
                    ></div>
                    
                    <div class="form-group">
                    <label for="comment_text">Your comment</label>
                    <textarea id="comment_text"
                              class="form-control" 
                              rows=3
                              cols=40
                              v-model="new_comment"
                    ></textarea>
                </div>
                <button class="btn btn-sm btn-primary" type="submit">Submit</button>
            </form>
        </div>
    </div>
    `
})


// Single comment component
Vue.component('single-comment', {

    props: {
        comment: {
            type: Object,
            required: true
        }
    },
    template: `
    <div class="comment">
        <div class="card">
            <div class="card-header">
                User: {{ comment.username }}
            </div>
            <div class="card-body">
                <p> {{ comment.content }} </p>
            </div>
        </div>
    </div>
    ` 
})

var app = new Vue( {
    el: '#app',
    data: {
        comments: [
            {username: 'Batman', content: 'First comment!'},
            {username: 'Catwoman', content: 'Second comment!'},
            {username: 'Ironman', content: 'New armor arrived!'},
            {username: 'Superman', content: 'Fourth comment!'},
        ]
    },

    methods: {
        addNewComment(new_comment) {
            this.comments.push(new_comment);
        }
    }
})