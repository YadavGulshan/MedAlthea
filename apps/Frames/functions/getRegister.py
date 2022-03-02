import requests

from .makerequest import makeRequest

mr = makeRequest()


def userRegister(userDetails):
    # response = mr.makePostRequest(mr.API + "/register/", userDetails)
    response = requests.post(mr.API + "/register/", json=userDetails)
    if response.status_code == 201:
        print("register success")
        return response
    elif response.status_code == 400:
        print("sorry something went wrong!!")
        print(response)
        return response
    else:
        print(response)
        return response
