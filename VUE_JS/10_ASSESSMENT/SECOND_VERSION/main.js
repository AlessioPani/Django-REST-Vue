Vue.component('to-do', {
    props: {
        tasks: {
            type: Array,
            required: true
        },
        amount: {
            type: Number,
            required: true
        }
    },

    data: function() {
        return {
            new_task: null,
            error: null
        }
    },

    methods: {
        submitTask() {
            if (this.new_task) {
                this.$emit('add-task', this.new_task);
                this.new_task = null;

                if (this.error) {
                    this.error = null;
                }
            } else {
                this.error = 'This field must be filled!'
            }
        },

        removeTaskComp(task) {
            this.$emit('remove-task', task);
            this.error = null;
        }

    },

    template: `
    <div class="container mt-1">
        <p><strong>Task counter: {{ amount }}</strong></p>

        <input type="text" 
               class="form-control" 
               placeholder="Add a new task" 
               v-model='new_task'
               @keyup.enter="submitTask">

        <p class="mt-1">{{ error }}</p>

        <div class="single-task"
             v-for="(task, index) in tasks"
             :task="task"
             :key="index">

            <div class="alert alert-success">
                {{ task }}
                <button type="button" 
                        class="close no-outline"
                        @click="removeTaskComp(task)">
                    <span>&times;</span>
                </button>
            </div>
        </div>

        <p v-if="amount === 0">To add a new task, fill the description field and press Enter.</p>
    </div>
    `
})

var app = new Vue({
    el: '#app',

    data: {
        tasks: [],
    },

    methods: {
        addNewTask(new_task) {
            this.tasks.push(new_task);
        },

        removeTask(task) {
            this.tasks.splice(this.tasks.indexOf(task), 1);
        }
    },

    computed: {
        taskCount() {
            return this.tasks.length;
        }
    }
})