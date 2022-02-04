# Import all required packages
import requests
# from requests.structures import CaseInsensitiveDict
import json as js

# username = input("Enter your username")
# password = input("Enter your password ")

getTokenUrl = "http://localhost:8000/api/token/"


def getTokens(username, password):
    userCredential = {
        "username": username,
        "password": password
    }
    tokens = requests.post(getTokenUrl, json=userCredential)

    print(tokens.status_code)
    filename = "userName.json"
    if tokens.status_code == 200:
        with open(filename, "w") as f:
            js.dump(tokens.json(), f)

    return tokens

    # headers = CaseInsensitiveDict()
    # token = ""
    # headers["Accept"] = "application/json"
    # headers["Authorization"] = "Bearer {}".format(token)
    #
    # resp = requests.get(url, headers=headers)
    #
    # print(resp.status_code)
