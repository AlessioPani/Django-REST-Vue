function getJSON(response) {
    data = response.json()
    return data;
}

function get_currency_rate(currency) {

    // console.log(currency);

    let url = 'https://api.exchangeratesapi.io/latest?symbols=' + currency;
    fetch(url)
        .then(getJSON)
        .then(data => {
            // console.log("Data: ", data)
            let rate = Object.values(data.rates)[0]
            document.querySelector('#exchange-results').innerHTML = `1.00 Euro are ${rate} ${currency}.`;
        })
        .catch(error => {
            // console.log("Error: ", error)
            document.querySelector('#exchange-results').innerHTML = `Error ${error}`;
        })

}

document.addEventListener('DOMContentLoaded', ()=> {
    document.querySelector('#form').onsubmit = event => {

        event.preventDefault();

        const currency = document.querySelector('#currency').value;

        get_currency_rate(currency);

        document.querySelector('#currency').value = "";
    }
})