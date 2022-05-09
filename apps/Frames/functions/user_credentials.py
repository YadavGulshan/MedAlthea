import requests

from .localdb import LocalDB
from .makerequest import makeRequest


class userCredentials:
    def __int__(self, name: str):
        self.mr = makeRequest(name)
        self.DB = LocalDB(name)

    def userRegister(self, userDetails: object):
        response = requests.post(self.mr.API + "/register/", json=userDetails)
        if response.status_code == 201:
            return response
        elif response.status_code == 400:
            return response
        else:
            return response

    def getTokens(self, username: str, password: str):
        user_credential = {
            "username": username,
            "password": password
        }

        tokens = self.mr.makePostRequest(self.mr.API + "/token/", user_credential)
        if tokens.status_code == 200:
            access = tokens.json().get("access")
            refresh = tokens.json().get("refresh")
            self.DB.addNewToken(access, refresh)
        return tokens.status_code
