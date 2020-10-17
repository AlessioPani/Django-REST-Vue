document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("button").onclick = counter;
})

// CLASSIC FUNCTION DEFINITION
// document.addEventListener("DOMContentLoaded", function() {
//     document.querySelector('#nameform').onsubmit = function(e) {
//         // e.preventDefault();
//         const name = document.querySelector("#nameinput").value;
//         alert(`Your name is ${name}`);
//         document.querySelector("#nameinput").value = '';

//         return false
//     };
// })

// ARROW FUNCTION DEFINITION
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('#nameform').onsubmit = e => {
        // e.preventDefault();
        const name = document.querySelector("#nameinput").value;
        alert(`Your name is ${name}`);
        document.querySelector("#nameinput").value = '';

        return false
    };
})

let array_number = [5, 7, 11, 13];
let cnt = 0;

function counter() {
    cnt++;
    if (array_number.includes(cnt)) {
        alert('The current value can be found in the array!');
    } else {
        console.log(cnt);
    }
    document.querySelector("#counter_h").innerHTML = cnt;
}

function hello_world() {
    let name = prompt("Insert your name")
    // alert('Ciao ' + name + '!')
    alert(`Hello ${name}!`)
}
//hello_world()

function change_message() {
    // querySelector select the first entry of 'h1'
    document.querySelector('h1').innerHTML = 'Goodbye!'; 
}