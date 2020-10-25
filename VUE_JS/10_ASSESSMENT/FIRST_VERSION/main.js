var app = new Vue({
    el: '#app',

    data: {
        task: null,
        tasks: [],
        counter: 0,
        error: null
    },
    methods: {
        
        onSubmit() {
            if (this.task) {
                this.counter = this.tasks.push(this.task);
                this.task = null;

                if (this.error) {
                    this.error = null;
                }
            } else {
                this.error = "Task description cannot be empty!";
            }
        },

        taskDelete(index) {
            this.tasks.splice(index, 1);
            this.counter--;

            if (this.error) {
                this.error = null;
            }
        }
    }
})