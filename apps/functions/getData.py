import json

from datetime import datetime

import requests
from requests.structures import CaseInsensitiveDict
import requests as rs
import json as js
import LocalDB


con = LocalDB.LocalDB()


def makerequest(token, url):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer {}".format(token)
    resp = requests.get(url, headers=headers)

    return resp


def searchMedicine(MedicineName):
    url = "http://localhost:8000/api/token/"
    res = con.getAccessToken()
    token = res[1]

    makerequest()


def searchUserName(username):
    res = con.getAccessToken()

    token = res[0]


def calculateDistance(lat1, long1, lat2, long2):
    token = res[0]


def getNearByShop():
    con = LocalDB.LocalDB()
    res = con.getAccessToken()

    token = res[0]
