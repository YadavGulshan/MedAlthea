# MedAlthea

Medical API doc

> **Note:** API endpoints starts with `/api/`

**Listing Medical Shops**

> Use `/`, i.e. http://yourdomain.com/api/ with access token in the header.
> 
> ```python
> try:
>     response = await get("url", 
>             HTTP_AUTHORIZATION="Bearer access_token" })
>     if response.status_code == 200:
>         print(response.body)
>     else:
>         raise Exception("Unauthorized")
> except Exception as e:
>     print(e)
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

**Add Medical Shop**

> Perform a `POST` request on `/` endpoint with the details.
> 
> **Example Request Payload:**
> 
> ```json
> {
>   "name": "A very good medical",
>   "address": "A real address",
>   "pincode": "129340",
>   "latitude": 1.53,
>   "longitude": 1.62662,
>   "phone": "+916665565656",
>   "email": "somemail@fh.com"
> }
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

**Updating the medical shop details**

For updating the medical shop details, Just  perform the `PUT` request on `/$id` endpoint.

**Note:** *You need to passin the medical ID and proper access token to update any value.* Right now backend is not accepting the update in email or phone number.

**Deleting the Medical shop**

Same as above but here, use the `DELETE` method.
