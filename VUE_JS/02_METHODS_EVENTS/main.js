var app = new Vue({
    el: '#app',
    data: {
        lesson: 'Events and Methods in Vue.js',
        counter: 0,
    },
    methods: {
        increaseCounter() {
            this.counter++;
            console.log(this.counter);
            if (this.counter === 10) {
                alert('Counter = 10!');
            }
        },
        
        overTheBox() {
            console.log('Mouse over the green box!');
        }
    }
})