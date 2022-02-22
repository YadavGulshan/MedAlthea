## MedAlthea

## USER API doc

**Note:** All the doc related to auth is valid here too.

**Table of Content:**

- [Getting the list of all the medicines](#getting-the-list-of-all-the-medicines)
- [Getting the list of medicine in nearby shops](#getting-the-list-of-medicine-in-nearby-shops)
- [Creating Medicine](#creating-medicine)
- [Updating Medicine](#updating-medicine)
- [Deleting Medicine](#deleting-medicine)
  
  

### Getting the list of all the medicines

Perform a `GET` request on `medicine/` enpoint.

**Example Code:**

> ```python
> import requests
> 
> reqUrl = "http://127.0.0.1:8000/api/medicine"
> 
> headersList = {
>  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NDY0NzcwLCJpYXQiOjE2NDU0NjI5NzAsImp0aSI6IjRhM2U5N2VmZDdjODRkZGJiYThmNzJjYTlkMjczNWNmIiwidXNlcl9pZCI6OSwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5tZU9mTWVkaWNhbFNob3BPd25lciIsImVtYWlsIjoiZXhhbXB3bGUyQGVtYWlsLmNvbSJ9.zcYpXu6phM1L-XXZpKWr6E_MgEDCmO_10-IiYr6h-Hg" 
> }
> 
> payload = ""
> 
> response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
> ```



____

### Getting the list of medicine in nearby shops

Perform a `POST` request on `nearbymedicine/` enpoint with medicine name and pincode.

> ```python
> import requests
> 
> reqUrl = "http://127.0.0.1:8000/api/nearbymedicine/"
> 
> headersList = {
>  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NDY0NzcwLCJpYXQiOjE2NDU0NjI5NzAsImp0aSI6IjRhM2U5N2VmZDdjODRkZGJiYThmNzJjYTlkMjczNWNmIiwidXNlcl9pZCI6OSwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5tZU9mTWVkaWNhbFNob3BPd25lciIsImVtYWlsIjoiZXhhbXB3bGUyQGVtYWlsLmNvbSJ9.zcYpXu6phM1L-XXZpKWr6E_MgEDCmO_10-IiYr6h-Hg",
>  "Content-Type": "application/json" 
> }
> 
> payload = json.dumps({
>     "name": "Medicine Name",
>     "pincode": 40061
> })
> 
> response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
> ```



___

### Creating Medicine

Perform a `POST` request on `medicine/` enpoint with the payload similar to this,

```json
{
    "medicalId": 8,
    "name": "Gulkand",
    "description": "IDK",
    "price": 69,
    "quantity": 100
}
```

**Python Example:**

> ```python
> import requests
> 
> reqUrl = "http://127.0.0.1:8000/api/medicine/"
> 
> headesList = {
>  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NTQ2ODExLCJpYXQiOjE2NDU1NDUwMTEsImp0aSI6IjdiZDY0YWU2NmQ0ZjRiZTViY2VlYmU1NzJjNzIxMTI5IiwidXNlcl9pZCI6OCwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5hbWVPZk1lZGljYWxTaG9wT3duZXIiLCJlbWFpbCI6ImV4YW1wbGUyQGVtYWlsLmNvbSJ9.lwdpnYzM_vYbZsWFCbpPjmdbolhmLi__yAupywIxngs",
>  "Content-Type": "application/json" 
> }
> 
> payload = json.dumps({
>     "medicalId": 8,
>     "name": "Gulkand",
>     "description": "IDK",
>     "price": 69,
>     "quantity": 100
>  
>   })
> 
> response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
> 
> 
> ```

**Status Codes to look for**:

> **201 Created:**
> 
> > States that medicine is successfully created for your medical shop

> **406 Not Acceptable:**
> 
> > If the current user is not a owner of the medical shop, then backend will generate this response.
> > 
> > > Or you didn't specified the required payloads.
> > 
> > **Payload:**
> > 
> > ```json
> > {
> >     "medicalId": 78,
> >     "name": "Gulkand",
> >     "description": "IDK",
> >     "price": 69,
> >     "quantity": 100
> >  }
> > ```

____

### Updating Medicine

Perform `PUT` request on `/medicine/<medicine_id>/` endpoint with the payload similar to this,

```json
{
    "name": "Gulkand hmm",
    "description": "IDK",
    "price": 679,
    "quantity": 50,
    "medicalId": 1
}
```

**Python Example:**

> ```python
> import requests
> 
> reqUrl = "http://127.0.0.1:8000/api/medicine/5/"
> 
> headersList = {
>  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NTQ4NjE1LCJpYXQiOjE2NDU1NDY4MTUsImp0aSI6IjQ3MzBhODAzY2YyZDQ2NDdhMDNjMTdiNWI3NTAyZTk4IiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5hbWVPZk1lZGljYWxTaG9wT3duZXIiLCJlbWFpbCI6ImV4YW1wbGUyQGVtYWlsLmNvbSJ9.f516O_7_dKTeIWIt7nUtcbTYzhpYIahXgrdf-e9nyTY",
>  "Content-Type": "application/json" 
> }
> 
> payload = json.dumps({
>     "name": "Gulkand hmm",
>     "description": "IDK",
>     "price": 679,
>     "quantity": 50,
>     "medicalId": 1
>  })
> 
> response = requests.request("PUT", reqUrl, data=payload,  headers=headersList)
> 
> 
> ```
> 
> Look for **400 Bad Request**
> 
> > You are suppose to fill in all the information like shown above.
> > 
> > **Reason:**
> > 
> > > That's how serializer works. :/

____

### Deleting Medicine

Perform `DELETE` reques on `/medicine/<medicine_id_you_want_to_delete>`

**Expected Response:**

> Status: **202 Accepted**

Remember that you need to proved the access token, else backend won't allow you to do this transaction.

**Noticed Bug:**

> When you'll try updating the medicine which doesn't exist, backend gives you a 500 response.
> 
> > Fixes applied for now:
> > 
> > [Bug Fixes!! by YadavGulshan · Pull Request #47 · YadavGulshan/MedAlthea · GitHub](https://github.com/YadavGulshan/MedAlthea/pull/47/commits/26c85e7ca3332652a1c8576abde92fed604f7067)

____

### Searching the medicine

____

### 