# Request example using Requests module to communicate with an external
# service; in this case will be a basic request to Exchangeratesapi's APIs.

import requests


def main():
    payload = {'base': 'USD', 'symbols': 'GBP'}
    response = requests.get("https://api.exchangeratesapi.io/latest",
                            params=payload)
    if response.status_code != 200:
        raise Exception("Error request!")
    data = response.json()
    print("JSON: ", data)


if __name__ == "__main__":
    main()
