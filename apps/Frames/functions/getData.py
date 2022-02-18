from requests.structures import CaseInsensitiveDict
import requests as rs

from localdb import LocalDB

con = LocalDB()

def makerequest(self, token, url, body):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer {}".format(token)
    resp = rs.get(url, headers=headers, json=body)
    return resp


def searchMedicine(self, MedicineName):
    data = self.con.getAccessToken()
    resp = self.makerequest(
        data[0],
        "http://localhost:8000/api/medicine/search/?search={}".format(MedicineName),
        {},
    )
    return resp


def searchUserName(self, username):
    resp = self.makerequest(
        {},
        "http://localhost:8000/api/register/search/?username={}".format(username),
        {},
    )
    return resp


def getNearByShop(self, pincode):
    data = self.con.getAccessToken()
    return self.makerequest(
        data[0], "http://localhost:8000/api/nearbymedical/", pincode
    )


def addMedicine():
    pass

def getnewtoken():
    url = "http://localhost:8000/api/token/refresh/"
    token = con.getRefreshToken()
    refresh = {
        "refresh": token[0][0] 
    }
    resp = rs.post(url, json=refresh)
    con.addNewToken(resp.json().get("access"),resp.json().get("refresh"))
    