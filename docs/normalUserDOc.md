## MedAlthea

## USER API doc

**Note:** All the doc related to auth is valid here too.

### Getting the list of all the medicines

Perform a `GET` request on `medicine/` enpoint.

**Example Code:**

```python
import requests

reqUrl = "http://127.0.0.1:8000/api/medicine"

headersList = {
 "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NDY0NzcwLCJpYXQiOjE2NDU0NjI5NzAsImp0aSI6IjRhM2U5N2VmZDdjODRkZGJiYThmNzJjYTlkMjczNWNmIiwidXNlcl9pZCI6OSwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5tZU9mTWVkaWNhbFNob3BPd25lciIsImVtYWlsIjoiZXhhbXB3bGUyQGVtYWlsLmNvbSJ9.zcYpXu6phM1L-XXZpKWr6E_MgEDCmO_10-IiYr6h-Hg" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
```

____

### Getting the list of medicine in nearby shops

Perform a `POST` request on `nearbymedicine/` enpoint with medicine name and pincode.

```python
import requests

reqUrl = "http://127.0.0.1:8000/api/nearbymedicine/"

headersList = {
 "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NDY0NzcwLCJpYXQiOjE2NDU0NjI5NzAsImp0aSI6IjRhM2U5N2VmZDdjODRkZGJiYThmNzJjYTlkMjczNWNmIiwidXNlcl9pZCI6OSwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5tZU9mTWVkaWNhbFNob3BPd25lciIsImVtYWlsIjoiZXhhbXB3bGUyQGVtYWlsLmNvbSJ9.zcYpXu6phM1L-XXZpKWr6E_MgEDCmO_10-IiYr6h-Hg",
 "Content-Type": "application/json" 
}

payload = json.dumps({
    "name": "Medicine Name",
    "pincode": 40061
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)


```

___

### Creating Medicine

____

### Updating Medicine

____

### Deleting Medicine

____




