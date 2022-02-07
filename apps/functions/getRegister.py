import requests as rs

registerUrl = 'http://127.0.0.1:8000/api/register/'


def userLogin(userDetails):
    # username = userDetails.username
    # password = userDetails.password
    # password2 = userDetails.password2
    # email = userDetails.email
    # firstname = userDetails.firstname
    # lastname = userDetails.lastname

    response = rs.post(registerUrl, json=userDetails)
    res = response.json()
    if response.status_code == 200:
        print('register success')

    # elif response.status_code == 400:
    #     if res['email'] | res['username']:
    #         print(res['email'])
    #         print(res['username'])
    else:
        print(res)
