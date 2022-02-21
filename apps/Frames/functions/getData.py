from requests.structures import CaseInsensitiveDict
import requests as rs

from localdb import LocalDB

db = LocalDB()


def makerequest(token, url, body):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer {}".format(token)
    resp = rs.get(url, headers=headers, json=body)
    return resp


def searchMedicine(MedicineName):
    data = db.getAccessToken()
    resp = makerequest(
        data[0],
        "http://localhost:8000/api/medicine/search/?search={}".format(MedicineName),
        {},
    )
    return resp


def checkAvailableUser(username):
    resp = makerequest(
        {},
        "http://localhost:8000/api/register/search/?username={}".format(username),
        {},
    )
    if resp.status_code == 201:
        return True
    else:
        return False


def getNearByShop(pincode):
    data = db.getAccessToken()
    return makerequest(
        data[0], "http://localhost:8000/api/nearbymedical/", pincode
    )


def addMedicine():
    pass


def getNewToken():
    token = db.getRefreshToken()
    refresh = {
        "refresh": token[0][0]
    }
    resp = rs.post("http://localhost:8000/api/token/refresh/", json=refresh)
    db.addNewToken(resp.json().get("access"), resp.json().get("refresh"))
