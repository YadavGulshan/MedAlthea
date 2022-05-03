# Trending Drug page view
**Python code for refrence:**
```python 
import requests

reqUrl = "http://127.0.0.1:8000/api/popularmedicine/?pincode=400607"

headersList = {
 "Authorization": "Bearer <TOKEN>" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)
```

**Output:**
```json
[
  {
    "name": "dolo",
    "count": 3
  }
]
```

Rank the one with the highest count!