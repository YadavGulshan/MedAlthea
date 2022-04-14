import requests

from .makerequest import makeRequest


def userRegister(userDetails, name):
    mr = makeRequest(name)
    # response = mr.makePostRequest(mr.API + "/register/", userDetails)
    response = requests.post(mr.API + "/register/", json=userDetails)
    if response.status_code == 201:
        return response
    elif response.status_code == 400:
        return response
    else:
        return response
