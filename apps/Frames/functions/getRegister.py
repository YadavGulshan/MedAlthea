from .makerequest import makeRequest

mr = makeRequest()


def userLogin(userDetails):
    response = mr.makePostRequest(mr.API + "/register/", userDetails)

    if response.status_code == 201:
        print("register success")
        return response
    elif response.status_code == 400:
        print("sorry something went wrong!!")
        print(response)
    else:
        print(response)
