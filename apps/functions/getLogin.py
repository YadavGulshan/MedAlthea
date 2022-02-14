import requests
from apps.functions.LocalDB import LocalDB

getTokenUrl = "http://localhost:8000/api/token/"


def getTokens(username, password):
    user_credential = {
        "username": username,
        "password": password
    }
    try:
        tokens = requests.post(getTokenUrl, json=user_credential)
        DB = LocalDB()
        access = tokens.json().get('access')
        refresh = tokens.json().get('refresh')
        DB.addNewToken(access, refresh)

        return tokens

    except Exception as e:
        print(e)
        return {}


getTokens("rahulyadav", "1234")
