document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll('.color-change').forEach( button => {
        button.onclick = () => {
            document.querySelector('#box').style.background = button.dataset.color;
        }}
        )
    })

    // document.querySelector('#green').onclick = () => {
    //     document.querySelector('#box').style.background = 'green';
    // }

    // document.querySelector('#red').onclick = () => {
    //     document.querySelector('#box').style.background = 'red';
    // }

    // document.querySelector('#orange').onclick = () => {
    //     document.querySelector('#box').style.background = 'orange';
    // }