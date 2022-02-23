import requests as rs

registerUrl = "http://127.0.0.1:8000/api/register/"


def userLogin(userDetails):

    response = rs.post(registerUrl, json=userDetails)
    res = response.json()
    if response.status_code == 201:
        print("register success")
        return response
    elif response.status_code == 400:
        print("sorry something went wrong!!")
        print(response.json())
    else:
        print(res)
