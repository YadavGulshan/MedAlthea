from requests.structures import CaseInsensitiveDict
import requests as rs

from .localdb import LocalDB

db = LocalDB()


def makerequest(token, url, body):
    try:
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer {}".format(token)
        resp = rs.get(url, headers=headers, json=body)
        if resp.status_code==200:
            return resp
        else:
            raise Exception("Unauthorized")
    except Exception as e:
        print(e)


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


def addMedicine(medicine: object):
    # {
    #     "name": [
    #         "This field is required."
    #     ],
    #     "description": [
    #         "This field is required."
    #     ],
    #     "price": [
    #         "This field is required."
    #     ],
    #     "quantity": [
    #         "This field is required."
    #     ],
    #     "medicalId": [
    #         "This field is required."
    #     ]
    # }
    pass


def getNewToken():
    token = db.getRefreshToken()
    refresh = {
        "refresh": token[0]
    }
    resp = rs.post("http://localhost:8000/api/token/refresh/", json=refresh)
    if resp.status_code==200:
        db.addNewToken(resp.json().get("access"), resp.json().get("refresh"))


def allMedicalShop():
    data = db.getAccessToken()
    resp = makerequest(data[0], "http://localhost:8000/api/", {})
    if resp.status_code == 200:
        return resp
    else:
        getNewToken()
