from .makerequest import makeRequest

make = makeRequest("userToken")


def searchMedicine(medicine_name):
    """ Data required are Medicine Name """

    resp = make.GetRequest(
        make.API + "/medicine/search/?search={}".format(medicine_name), {})
    return resp


def getNearByShop(medicine, pincode, lat, lon):
    """This function required user's area code or pincode
    through which this function will return nearby shop to user"""
    return make.GetRequest(
        make.API + "/nearbymedicine/?name={}&pincode={}&latitude={}&longitude={}".format(medicine, 400601, lat, lon))


def allMedicalShop():
    resp = make.GetRequest(make.API + "/", {})
    print(resp)
    if resp.status_code == 200:
        return resp
    else:
        print("Error")


def getAllMedicines():
    return make.GetRequest(make.GetRequest(make.API + "/medicine/"))
