import requests


def client():
    token_h = 'Token 7833d3d3b15ac65f4e5663f9acd4c3995dcb02d9'

    # credentials = {
    #     'username': 'admin',
    #     'password': 'ciaociao'
    # }

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/',
    #                          data=credentials)

    headers = {
        "Authorization": token_h
    }

    response = requests.get('http://127.0.0.1:8000/api/profiles/',
                            headers=headers)

    print("Status code: ", response.status_code)

    response_data = response.json()

    print(response_data)


if __name__ == "__main__":
    client()
