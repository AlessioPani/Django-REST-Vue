function get_currency_rate(currency) {

    console.log(currency);

    let url = 'https://api.exchangeratesapi.io/latest?symbols=' + currency;

    // const config = {
    //     method = 'POST', // GET, POST, PUT, ...
    //     body: JSON.stringify(data)
    // }
    // fetch(url, config);

    fetch(url)
        .then(function(response) {
            console.log('Status:', response.status);
            response.json()
                .then(function(data) {
                    console.log("Fetch result", data)
                })
        })

}

get_currency_rate("USD");