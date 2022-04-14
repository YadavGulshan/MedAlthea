from .localdb import LocalDB
from .makerequest import makeRequest


def getTokens(username, password, name):
    mr = makeRequest(name)
    user_credential = {
        "username": username,
        "password": password
    }

    tokens = mr.makePostRequest(mr.API + "/token/", user_credential)
    DB = LocalDB(name)
    if tokens.status_code == 200:
        access = tokens.json().get("access")
        refresh = tokens.json().get("refresh")
        DB.addNewToken(access, refresh)
    return tokens.status_code
