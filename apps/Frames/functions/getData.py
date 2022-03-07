import requests as rs

from .makerequest import makeRequest

mr = makeRequest()


def searchMedicine(medicine_name):
    """ Data required are Medicine Name """

    resp = mr.makeGetRequest(mr.API + "/medicine/search/?search={}".format(medicine_name), {})
    return resp


def checkAvailableUser(username):
    """This function will return
    whether the given username for registration is available for new registration"""
    resp = rs.get(mr.API + "/register/search/?username={}".format(username))
    return resp


def getNearByShop(pincode):
    """This function required user's area code or pincode
    through which this function will return nearby shop to user"""
    return mr.makeGetRequest(mr.API + "/nearbymedical/", pincode)


def addMedicine(medicine: object):
    """Data required are "name", "description", "price", "quantity", "medicalId" """
    return mr.makePostRequest(mr.API + "/medicine/", medicine)


def createMedical(medical: object):
    """Data required are Medical "name", "address", "pincode", "latitude", "longitude", "phone" Number, "email" """
    return mr.makePostRequest(mr.API + "/", medical)


def allMedicalShop():
    resp = mr.makeGetRequest(mr.API + "/", {})
    print(resp)
    if resp.status_code == 200:
        return resp
    else:
        print("Error")


def getMedicine(medical_id):
    resp = mr.makeGetRequest(mr.API + "/mymedical/{}/".format(medical_id), {})
    return resp


def getMyMedical():
    resp = mr.makeGetRequest(mr.API + "/mymedical/", {})
    return resp

details=["first name","last name","pincode","Address","Phone number","email"] 
def getProfileDetails(details):
    resp = mr.makeGetRequest(mr.API + "/medicalProfile/{}/".format(details),{})
    return resp

