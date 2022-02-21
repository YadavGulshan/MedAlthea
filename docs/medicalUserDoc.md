# MedAlthea

## Medical API doc

**Note:** API endpoints starts with `/api/`

**Table of Content:**

  - [Listing Medical Shops](#listing-medical-shops)
  - [Listing Medical Shops](#listing-medical-shops)
  - [Add Medical Shop](#add-medical-shop)
  - [Listing the owners medical shops](#listing-the-owners-medical-shops)
  - [Updating the medical shop details](#updating-the-medical-shop-details)
  - [Deleting the Medical shop](#deleting-the-medical-shop)
  - [Getting the list of nearby medical shops](#getting-the-list-of-nearby-medical-shops)
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

# Getting the list of nearby medical shops

This is a recommended method for building your application.

Leme create some test medical shops...

> `GET` on `/`
> 
> ```json
> [
>   {
>     "medicalId": 2,
>     "createdAt": "2022-02-21T15:56:01.689379Z",
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
>   },
>   {
>     "medicalId": 3,
>     "createdAt": "2022-02-21T17:08:27.827885Z",
>     "name": "medical 1",
>     "address": "some addr",
>     "pincode": 400607,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   },
>   {
>     "medicalId": 4,
>     "createdAt": "2022-02-21T17:08:36.924023Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 400157,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   },
>   {
>     "medicalId": 5,
>     "createdAt": "2022-02-21T17:08:41.851574Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 400610,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   },
>   {
>     "medicalId": 6,
>     "createdAt": "2022-02-21T17:08:47.630041Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 400670,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   },
>   {
>     "medicalId": 7,
>     "createdAt": "2022-02-21T17:08:52.503319Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 400621,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   },
>   {
>     "medicalId": 8,
>     "createdAt": "2022-02-21T17:08:57.822702Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 400603,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   },
>   {
>     "medicalId": 9,
>     "createdAt": "2022-02-21T17:09:13.387826Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 400699,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   },
>   {
>     "medicalId": 10,
>     "createdAt": "2022-02-21T17:09:20.650815Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 4006156,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   },
>   {
>     "medicalId": 11,
>     "createdAt": "2022-02-21T17:09:26.952719Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 400606,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   },
>   {
>     "medicalId": 12,
>     "createdAt": "2022-02-21T17:09:35.118131Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 401564,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   }
> ]
> ```

**Sorted Example:**

> **Note:** You have to perform a `POST` request with pincode in body on `nearbymedical` enpoint

```python
import requests

reqUrl = "http://127.0.0.1:8000/api/nerbymedical/"

headersList = {
 "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NDY0NzcwLCJpYXQiOjE2NDU0NjI5NzAsImp0aSI6IjRhM2U5N2VmZDdjODRkZGJiYThmNzJjYTlkMjczNWNmIiwidXNlcl9pZCI6OSwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5tZU9mTWVkaWNhbFNob3BPd25lciIsImVtYWlsIjoiZXhhbXB3bGUyQGVtYWlsLmNvbSJ9.zcYpXu6phM1L-XXZpKWr6E_MgEDCmO_10-IiYr6h-Hg",
 "Content-Type": "application/json" 
}

payload = json.dumps({
    "pincode": 40061
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
```

> **In this example you see I have only passed 40061 not the whole pincode.**
> 
> **Why?**
> 
> > Because we're looking for nearby medical shops, and there's high chance that aren't any. Because our database is not populated for them as of now.
> 
> One thing you can do is, you can perform a check for the exact pincode. If you get the response of lenght less than 5 or something, depending on your needs.
> 
> You can then re-request the api with shorted pincode.

> **Example Response:**
> 
> ```json
> [
>   {
>     "medicalId": 5,
>     "createdAt": "2022-02-21T17:08:41.851574Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 400610,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   },
>   {
>     "medicalId": 10,
>     "createdAt": "2022-02-21T17:09:20.650815Z",
>     "name": "medical 2",
>     "address": "some addr",
>     "pincode": 4006156,
>     "latitude": 1.66,
>     "longitude": 1.66665,
>     "phone": "+914564666545",
>     "email": "email@email2.com",
>     "website": "",
>     "image": null,
>     "user": 8
>   }
> ]
> ```
