# Request example using Requests module to communicate with an external
# service; in this case will be a GET request to Google's homepage.

import requests


def main():
    response = requests.get("http://www.google.com")
    print("\nStatus code: ", response.status_code)
    print("\nHeaders: ", response.headers)
    print("\nContent Type: ", response.headers['Content-Type'])
    # print("\nContent: ", response.text)


if __name__ == "__main__":
    main()
