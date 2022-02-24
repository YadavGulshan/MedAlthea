import datetime
from requests.structures import CaseInsensitiveDict
import requests as rs

from .localdb import LocalDB

db = LocalDB()
API = "http://localhost:8000/api"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"


def is_valid(time):
    lastUsed = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
    today = datetime.datetime.now()
    # print(today, lastUsed)
    day = today - lastUsed
    print(day)
    if day > datetime.timedelta(minutes=30):
        getNewToken()
        print("get new token")
    else:
        print("valid")


def makeGetRequest(url, body):
    token = db.getAccessToken()
    # [(access token, last time used)]

    # checking whether access token is valid or not if not then get new token!!
    is_valid(token[0][1])
    token = db.getAccessToken()
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
    is_valid(token[0][1])
    token = db.getAccessToken()

    try:
        headers["Authorization"] = "Bearer {}".format(token[0][0])
        resp = rs.post(url, headers=headers, json=body)
        if resp.status_code == 201:
            return resp
    except Exception as e:
        print(e)


def searchMedicine(medicineName):
    """ Data required are Medicine Name """

    resp = makeGetRequest(API + "/medicine/search/?search={}".format(medicineName), {})
    return resp


def checkAvailableUser(username):
    """This function will return
    whether the given username for registration is available for new registration"""
    resp = rs.get(API + "/register/search/?username={}".format(username))
    return resp


def getNearByShop(pincode):
    """This function required user's area code or pincode
    through which this function will return nearby shop to user"""
    return makeGetRequest(API + "/nearbymedical/", pincode)


def addMedicine(medicine: object):
    """Data required are "name", "description", "price", "quantity", "medicalId" """
    return makePostRequest(API + "/medicine/", medicine)


def createMedical(medical: object):
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
    print(resp)
    if resp.status_code == 200:
        return resp
    else:
        print("Error")

# print(createMedical(
#     {
#         "name": "A very good medical",
#         "address": "A real address",
#         "pincode": "129340",
#         "latitude": 1.53,
#         "longitude": 1.62662,
#         "phone": "+916665565656",
#         "email": "somemail@fh.com"
#     }))
