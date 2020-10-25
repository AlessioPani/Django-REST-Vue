var app = new Vue( {
    el: '#app',
    data: {
        first_name: 'Mario',
        last_name: 'Rossi'
    },
    methods: {
        getRandomNumber() {
            return Math.random()
        }
    },
    computed: {
        getRandomComputed() {
            return Math.random()
        },

        getFullName() {
            return `${this.first_name} ${this.last_name}`
        },
        
        getReversedFullName() {
            first = this.first_name.split("").reverse().join("")
            last = this.last_name.split("").reverse().join("")
            return `${first} ${last}`
        }
    }
});