from requests.structures import CaseInsensitiveDict
import requests as rs
import LocalDB

con = LocalDB.LocalDB()


def makerequest(token, url, body):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer {}".format(token)
    resp = rs.get(url, headers=headers, json=body)
    return resp


def searchMedicine(MedicineName):
    data = con.getAccessToken()
    resp = makerequest(data[0], "http://localhost:8000/api/medicine/search/?search={}".format(MedicineName), {})
    return resp


def searchUserName(username):
    resp = makerequest({}, "http://localhost:8000/api/register/search/?username={}".format(username), {})
    return resp


def getNearByShop(pincode):
    data = con.getAccessToken()
    return makerequest(data[0], "http://localhost:8000/api/nearbymedical/", pincode)

def addMedicine():
    pass
