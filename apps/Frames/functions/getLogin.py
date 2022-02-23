import requests
from .localdb import LocalDB

getTokenUrl = "http://127.0.0.1:8000/api/token/"


def getTokens(username, password):
    user_credential = {
        "username": username,
        "password": password
    }
    try:
        tokens = requests.post(getTokenUrl, json=user_credential)
        DB = LocalDB()
        access = tokens.json().get("access")
        refresh = tokens.json().get("refresh")
        if tokens.status_code == 200:
            DB.addNewToken(access, refresh)
        print(tokens)
        return tokens.status_code

    except Exception as e:
        print(e)
        return {}
