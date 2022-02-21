# MedAlthea

## Medical API doc

**Note:** API endpoints starts with `/api/`

### Listing Medical Shops

Use `/`, i.e. http://yourdomain.com/api/ with access token in the header.

> ```python
> import requests
> 
> reqUrl = "http://127.0.0.1:8000/api/"
> 
> headersList = {
>  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NDYwNjY1LCJpYXQiOjE2NDU0NTg4NjUsImp0aSI6Ijg3MTEzYzMzYjlkNTQyZWQ4OTY5NDBmZDQzNDg5MGY2IiwidXNlcl9pZCI6OCwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5hbWVPZk1lZGljYWxTaG9wT3duZXIiLCJlbWFpbCI6ImV4YW1wbGUyQGVtYWlsLmNvbSJ9.ujd0vN92iVp4qyZSNA0-SsPAagXQ-QaXtx8Ue1wQWOo",
>  "Content-Type": "application/json" 
> }
> 
> payload = ""
> 
> response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
> ```
> 
> **Possible response:**
> 
> ```json
> [
>   {
>     "medicalId": 1,
>     "createdAt": "2022-02-04T14:19:30.555131Z",
>     "name": "Gulshan",
>     "address": "Somewhere on planet earth",
>     "pincode": 404557,
>     "latitude": 1.65,
>     "longitude": 6.616,
>     "phone": "+912562626262",
>     "email": "yadavgulshan4@gmail.com",
>     "website": "",
>     "image": "/media/images/logo_tfr7Mho.png",
>     "user": 2
>   }
> ]
> ```

____

### Add Medical Shop

Perform a `POST` request on `/` endpoint with the details.

> **Example Code:**
> 
> ```python
> import requests
> 
> reqUrl = "http://127.0.0.1:8000/api/"
> 
> headersList = {
>  "Authorization": "Bearer eyJ0eXASsPAagXQ-QaXtx8Ue1wQWOo.blablabla",
>  "Content-Type": "application/json" 
> }
> 
> payload = json.dumps({
>   "name": "A very good medical",
>   "address": "A real address",
>   "pincode": "129340",
>   "latitude": 1.53,
>   "longitude": 1.62662,
>   "phone": "+916665565656",
>   "email": "somemail@fh.com"
> })
> 
> response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
> ```
> 
> **Response:**
> 
> ```json
> {
>   "medicalId": 4,
>   "createdAt": "2022-02-19T11:53:31.443093Z",
>   "name": "A very good medical",
>   "address": "A real address",
>   "pincode": 129340,
>   "latitude": 1.53,
>   "longitude": 1.62662,
>   "phone": "+916665565656",
>   "email": "somemail@fh.com",
>   "website": "",
>   "image": null,
>   "user": 2
> }
> ```
> 
> > **Note:** *Backend won't ask for any user detail, it will automatically assign the medical shop to the owner of given access token passed in header.*

____

### Listing the owners medical shops

Perform a `GET` request on `mymedical/` enpoint with access token in the header.

**Example code:**

```python
import requests

reqUrl = "http://127.0.0.1:8000/i/mymedical/"

headersList = {
 "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NDYyNzUxLCJpYXQiOjE2NDU0NjA5NTEsImp0aSI6IjRiNjBkZjM5YzBiNjRlMDc4M2E5NDE2NDc5NjZiODlhIiwidXNlcl9pZCI6OCwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5hbWVPZk1lZGljYWxTaG9wT3duZXIiLCJlbWFpbCI6ImV4YW1wbGUyQGVtYWlsLmNvbSJ9.GAUv-t5dacaYJaeq_h10UcUQiCPeXwt46gv43krNhGE" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
```

> **Example response:**
> 
> Status: **200 OK**
> 
> ```json
> [
>  {
>  "medicalId": 1,
>  "createdAt": "2022-02-21T15:55:16.630799Z",
>  "name": "A very good medical",
>  "address": "A real address",
>  "pincode": 129340,
>  "latitude": 1.53,
>  "longitude": 1.62662,
>  "phone": "+916665565656",
>  "email": "somemail@fh.com",
>  "website": "",
>  "image": null,
>  "user": 8
>  }
> ]
> ```

____

### Updating the medical shop details

For updating the medical shop details, Just  perform the `PUT` request on `/$id` endpoint.

**Note:** *You need to passin the medical ID and proper access token to update any value.* Right now backend is not accepting the update in email or phone number.

**Example code:**

```python
import requests

reqUrl = "http://127.0.0.1:8000/api/1"

headersList = {
 "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NDYyNzUxLCJpYXQiOjE2NDU0NjA5NTEsImp0aSI6IjRiNjBkZjM5YzBiNjRlMDc4M2E5NDE2NDc5NjZiODlhIiwidXNlcl9pZCI6OCwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5hbWVPZk1lZGljYWxTaG9wT3duZXIiLCJlbWFpbCI6ImV4YW1wbGUyQGVtYWlsLmNvbSJ9.GAUv-t5dacaYJaeq_h10UcUQiCPeXwt46gv43krNhGE",
 "Content-Type": "application/json" 
}

payload = json.dumps({
    "medicalId": 1,
    "name": "A very good medical",
    "address": "A real address",
    "pincode": 129340,
    "latitude": 1.53,
    "longitude": 1.62662,
  })

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
```

> **Example Response:**
> 
> Status: **200 OK**
> 
> ```json
> [
>   {
>     "medicalId": 1,
>     "createdAt": "2022-02-21T15:55:16.630799Z",
>     "name": "A very good medical",
>     "address": "A real address",
>     "pincode": 129340,
>     "latitude": 1.53,
>     "longitude": 1.62662,
>     "phone": "+916665565656",
>     "email": "somemail@fh.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   }
> ]
> ```
> 
> This represents the updated value.

____

### Deleting the Medical shop

Same as above but here, use the `DELETE` method.

**Example code:**

```python
import requests

reqUrl = "http://127.0.0.1:8000/api/1"

headersList = {
 "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NDYyNzUxLCJpYXQiOjE2NDU0NjA5NTEsImp0aSI6IjRiNjBkZjM5YzBiNjRlMDc4M2E5NDE2NDc5NjZiODlhIiwidXNlcl9pZCI6OCwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5hbWVPZk1lZGljYWxTaG9wT3duZXIiLCJlbWFpbCI6ImV4YW1wbGUyQGVtYWlsLmNvbSJ9.GAUv-t5dacaYJaeq_h10UcUQiCPeXwt46gv43krNhGE",
 "Content-Type": "application/json" 
}

payload = json.dumps({
    "medicalId": 1,
    "name": "A very good medical",
    "address": "A real address",
    "pincode": 129340,
    "latitude": 1.53,
    "longitude": 1.62662,
    "phone": "+916665565656",
    "email": "somemnail@fh.com"
  })

response = requests.request("DELETE", reqUrl, data=payload,  headers=headersList)
```

> **Expected response:**
> 
> Status: **204 No Content**
> 
> ```json
> "Deleted"
> ```

# 
