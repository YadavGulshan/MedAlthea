import requests
from requests.structures import CaseInsensitiveDict

header = CaseInsensitiveDict()
header["Accept"] = "application/json"
accessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUxNjAwMjkxLCJpYXQiOjE2NTE1OTg0OTEsImp0aSI6ImZkNzY5NjEyNWM5YzRkMmI5NmEwMzc2Mjg4ZTkzZWYzIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJyYWh1bCIsImVtYWlsIjoieWFkYXZyYWh1bDgxNDFAeWFob28uY29tIn0.yHgSeeKRCJe75Z8shspOwHl-aPjYTBn1Ze7lobDnvuA"
header["Authorization"] = "Bearer {}".format(accessToken)
resp = requests.get(url="http://127.0.0.1:8000/api/popularmedicine/?pincode=421302", headers=header)
data = resp.json()
newList = sorted(data, key=lambda d: d["count"], reverse=True)
print(newList)
