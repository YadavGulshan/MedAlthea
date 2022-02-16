import requests

getTokenUrl = "http://localhost:8000/api/token/"


def getTokens(self, username, password):
    user_credential = {
        "username": username,
        "password": password
    }
    try:
        tokens = requests.post(getTokenUrl, json=user_credential)
        DB = functions.LocalDB()
        access = tokens.json().get("access")
        refresh = tokens.json().get("refresh")
        DB.addNewToken(access, refresh)

        return tokens

    except Exception as e:
        print(e)
        return {}

# if "__name__" == "__main__":
#     getLogin.getTokens("rahulyadav", "1234")
