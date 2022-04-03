import requests as rs

from .makerequest import makeRequest

make = makeRequest()


def searchMedicine(medicine_name):
    """ Data required are Medicine Name """

    resp = make.GetRequest(
        make.API + "/medicine/search/?search={}".format(medicine_name), {})
    return resp


def checkAvailableUser(username):
    """This function will return
    whether the given username for registration is available for new registration"""
    resp = rs.get(make.API + "/register/search/?username={}".format(username))
    return resp


def getNearByShop(pincode):
    """This function required user's area code or pincode
    through which this function will return nearby shop to user"""
    return make.GetRequest(make.API + "/nearbymedical/", pincode)


def addMedicine(medicine: object):
    """Data required are "name", "description", "price", "quantity", "medicalId" """
    return make.makePostRequest(make.API + "/medicine/", medicine)


def createMedical(medical: object, file):
    """Data required are Medical "name", "address", "pincode", "latitude", "longitude", "phone", "email" """
    return make.CreateMedicalPost(make.API + "/", medical, file)


def allMedicalShop():
    resp = make.GetRequest(make.API + "/", {})
    print(resp)
    if resp.status_code == 200:
        return resp
    else:
        print("Error")


def getMedicine(medical_id):
    resp = make.GetRequest(make.API + "/mymedical/{}/".format(medical_id))
    return resp


def getMyMedical():
    resp = make.GetRequest(make.API + "/mymedical/")
    return resp


def getMedicalDetails(medical_id):
    resp = make.GetRequest(make.API + "/{}/".format(medical_id))
    return resp.json()[0]


def getUserDetails():
    resp = make.GetRequest(make.API + "/user/")
    return resp


def getMedicineDetails(ID):
    return make.GetRequest(make.API + '/medicine/{}/'.format(ID))


def deleteMedicine(ID):
    return make.DeleteRequest(make.API + '/medicine/{}/'.format(ID))


def deleteMedical(ID):
    return make.DeleteRequest(make.API + '/{}/'.format(ID))


def updateMedicine(medicine: object, ID):
    return make.PutRequest(make.API + '/medicine/{}/'.format(ID), medicine)


def updateMedical(medical, ID):
    return make.PutRequest(make.API + '/{}/'.format(ID), medical)
