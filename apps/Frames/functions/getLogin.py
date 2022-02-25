import requests
from .localdb import LocalDB
from .makerequest import makeRequest

mr = makeRequest()


def getTokens(username, password):
    user_credential = {
        "username": username,
        "password": password
    }

    tokens = mr.makePostRequest(mr.API + "/api/token/", user_credential)
    DB = LocalDB()
    access = tokens.json().get("access")
    refresh = tokens.json().get("refresh")
    if tokens.status_code == 200:
        DB.addNewToken(access, refresh)
    print(tokens)
    return tokens.status_code

