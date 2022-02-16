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
        DB.addNewToken(access, refresh)

        return tokens

    except Exception as e:
        print(e)
        return {}


# token = getTokens("rahulyadav", "1234")
# print(token.status_code)
