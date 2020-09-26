# Request example using Requests module to communicate with an external
# service; in this case will be a complete request to Exchangeratesapi's
# APIs.

import requests


def main():
    base_currency = input("\nInsert the base currency: ").upper()
    symbol_currency = input("Insert the second currency: ").upper()
    payload = {'base': base_currency, 'symbols': symbol_currency}
    response = requests.get("https://api.exchangeratesapi.io/latest",
                            params=payload)
    if response.status_code != 200:
        raise Exception("Error request! Base or second "
                        "currency doesen't exist! Try again!")
    data = response.json()
    quotation = data['rates'][symbol_currency]

    print("\nDate: ", data['date'])
    print(f'1 {base_currency} => {quotation} {symbol_currency}')


if __name__ == "__main__":
    main()
