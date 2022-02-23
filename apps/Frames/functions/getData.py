import DateTime
from requests.structures import CaseInsensitiveDict
import requests as rs

from .localdb import LocalDB

db = LocalDB()
API = "http://localhost:8000/api"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"


def is_valid(time):
    lastUsed = DateTime.DateTime(time)
    today = DateTime.DateTime()
    day = lastUsed-today
    minutes = day * 60
    print(minutes)
    if minutes > 30:
        getNewToken()
        print("get new token")


def makeGetRequest(url, body):
    token = db.getAccessToken()
    # [(access token, last time used)]

    # checking whether access token is valid or not if not then get new token!!
    is_valid(token[0][1])
    try:
        headers["Authorization"] = "Bearer {}".format(token[0][0])
        resp = rs.get(url, headers=headers, json=body)
        if resp.status_code == 200:
            return resp
        else:
            raise Exception("Unauthorized")
    except Exception as e:
        print(e)


def makePostRequest(url, body):
    token = db.getAccessToken()
    try:
        headers["Authorization"] = "Bearer {}".format(token[0][0])
        resp = rs.post(url, headers=headers, json=body)
        if resp.status_code == 201:
            return resp
        # else:
        # raise Exception("Unauthorized")
        # print("hmmm")
    except Exception as e:
        print(e)


def searchMedicine(medicineName):
    """ Data required are Medicine Name"""

    resp = makeGetRequest(API + "/medicine/search/?search={}".format(medicineName), {})
    return resp


def checkAvailableUser(username):
    resp = rs.get(API + "/register/search/?username={}".format(username))
    return resp


def getNearByShop(pincode):
    return makeGetRequest(API + "/nearbymedical/", pincode)


def addMedicine(medicine: object):
    """Data required are "name", "description", "price", "quantity", "medicalId" """
    return makePostRequest(API + "/medicine/", medicine)


def addMedical(medical: object):
    """Data required are Medical "name", "address", "pincode", "latitude", "longitude", "phone" Number, "email" """
    return makePostRequest(API + "/", medical)


def getNewToken():
    token = db.getRefreshToken()
    resp = rs.post(API + "/token/refresh/", json={
        "refresh": token[0][0]
    })
    if resp.status_code == 200:
        db.addNewToken(resp.json().get("access"), resp.json().get("refresh"))
    return resp


def allMedicalShop():
    resp = makeGetRequest(API + "/", {})
    if resp.status_code == 401:
        print("something went wrong")
    else:
        return resp
