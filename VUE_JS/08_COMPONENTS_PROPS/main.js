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
    }
})