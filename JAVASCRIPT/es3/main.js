document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#color-change').onchange = function() {
        document.querySelector('#box').style.background = this.value; 
    }

})