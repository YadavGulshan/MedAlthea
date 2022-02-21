import requests as rs

registerUrl = "http://127.0.0.1:8000/api/register/"


def userLogin(userDetails):

    response = rs.post(registerUrl, json=userDetails)
    res = response.json()
    if response.status_code == 200:
        print("register success")
    elif response.status_code == 400:
        print("sorry something went wrong!!")
    else:
        print(res)
