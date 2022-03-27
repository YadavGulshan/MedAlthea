import datetime
import requests as rs
from requests.structures import CaseInsensitiveDict

from .localdb import LocalDB


class makeRequest:
    def __init__(self):
        self.db = LocalDB()
        self.API = "http://localhost:8000/api"
        self.headers = CaseInsensitiveDict()
        self.headers["Accept"] = "application/json"
        self.accessToken = ""

    def __checkAccessToken(self):
        token = self.db.getAccessToken()
        if not len(token) == 0:
            accessTokenLastUsed = token[0][1]
            self.is_valid(accessTokenLastUsed)
            token = self.db.getAccessToken()
            self.accessToken = token[0][0]

    def is_valid(self, time):
        lastUsed = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
        today = datetime.datetime.now()
        day = today - lastUsed
        if day > datetime.timedelta(minutes=30):
            self.getNewToken()

    def makeGetRequest(self, url, body):
        self.__checkAccessToken()
        try:
            self.headers["Authorization"] = "Bearer {}".format(self.accessToken)
            resp = rs.get(url, headers=self.headers, json=body)
            if resp.status_code == 200:
                return resp
            else:
                raise Exception("Unauthorized")
        except Exception as e:
            print(e)

    def makePostRequest(self, url, body):
        self.__checkAccessToken()
        try:
            self.headers["Authorization"] = "Bearer {}".format(self.accessToken)
            resp = rs.post(url, headers=self.headers, json=body, )
            if resp.status_code == 201:
                return resp
            else:
                return resp
        except Exception as e:
            print(e)

    def makePutRequest(self, url, body):
        self.__checkAccessToken()
        try:
            self.headers["Authorization"] = "Bearer {}".format(self.accessToken)
            resp = rs.put(url=url, headers=self.headers, json=body)
            if resp.status_code == 200:
                return resp
            else:
                raise Exception("Something went wrong")
        except Exception as e:
            print(e)

    def makeDeleteRequest(self, url, body):
        self.__checkAccessToken()
        try:
            self.headers["Authorization"] = "Bearer {}".format(self.accessToken)
            resp = rs.delete(url=url, headers=self.headers, json=body)
            return resp
        except Exception as e:
            print(e)

    def getNewToken(self):
        token = self.db.getRefreshToken()
        resp = rs.post(self.API + "/token/refresh/", json={
            "refresh": token[0][0]
        })
        if resp.status_code == 200:
            self.db.addNewToken(resp.json().get("access"), resp.json().get("refresh"))
        return resp

    def CreateMedicalPost(self, url, body, file):
        try:
            self.__checkAccessToken()
            self.headers["Authorization"] = "Bearer {}".format(self.accessToken)
            resp = rs.post(url, headers=self.headers, data=body, files=file)
            if resp.status_code == 201:
                return resp
            else:
                return resp
        except Exception as e:
            print(e)
