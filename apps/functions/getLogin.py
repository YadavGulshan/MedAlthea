
import requests
import json as js


getTokenUrl = "http://localhost:8000/api/token/"


class getLogin:
    def getTokens(username, password):
        user_credential = {
        "username": username,
        "password": password
    }
        tokens = requests.post(getTokenUrl, json=user_credential)
    
        print(tokens.status_code)
        filename = "userName.json"
        if tokens.status_code == 200:
            with open(filename, "w") as f:
                js.dump(tokens.json(), f)
    
        return tokens
