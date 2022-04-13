from makerequest import makeRequest

make = makeRequest("userToken")


def searchMedicine(medicine_name):
    """ Data required are Medicine Name """

    resp = make.GetRequest(
        make.API + "/medicine/search/?search={}".format(medicine_name), {})
    return resp


def getNearByShop(pincode):
    """This function required user's area code or pincode
    through which this function will return nearby shop to user"""
    return make.GetRequest(make.API + "/nearbymedical/", pincode)


def allMedicalShop():
    resp = make.GetRequest(make.API + "/", {})
    print(resp)
    if resp.status_code == 200:
        return resp
    else:
        print("Error")


def getUserDetails():
    resp = make.GetRequest(make.API + "/user/")
    return resp
