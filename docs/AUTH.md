# MedAlthea

## API Urls

> **Note**: *API urls starts with `domain.com/api/`*

**Table of content:**

  - [Register User](#register-user)
  - [Login User](#login-user)
  - [Refresh the tokens](#refresh-the-tokens)
### Register User

There are two types of User, 

1. Staff

2. Normal User

A staff can add as many Medical as he/she wants. But a normal user doesn't have such permissions.

> `register/`
> 
> **Expect 201 Created Responce**
> 
> > Perform a `POST` request here with,
> > 
> > ```json
> > {
> >   "username": "AUniqueUsername",
> >   "password": "AHardPassword1232",
> >   "password2": "AHardPassword1232",
> >   "email": "example@email.com",
> >   "first_name": "Gulshan",
> >   "last_name": "Yadav"
> > }
> > ```
> > 
> > >  Adding these value will register a **Normal User**.
> 
> > To register a **Staff**,
> > 
> > ```json
> > {
> >   "username": "AUniqueUsernameOfMedicalShopOwner",
> >   "password": "AHardPassword1232",
> >   "password2": "AHardPassword1232",
> >   "email": "example2@email.com",
> >   "first_name": "Gulshan",
> >   "last_name": "Yadav",
> >   "isStaff": true
> > }
> > ```
> 
> **Note:** *You have to perform a check for username existance everytime user tries a username.*
> 
> `register/search/`
> 
> **400**: States that username already exists
> 
> **201**: States that username is available
> 
> > Example
> > 
> > ```json
> > {
> >     "username": "gulshan45"
> > }
> > ```

____

### Login User

> **Note:** *After completing the registeration, service program shall perform a login request on behalf of user to get the `access token` and `refresh token`*
> 
> **But do remember that login credential should not be stored anywhere.** They should be disposed once their use of done.

> `token/`
> 
> **Expect 200 OK Response on Successfull login**
> 
> > Perform a `POST` request here with similar `JSON` body
> > 
> > ```json
> > {
> >     "username": "AUniqueUsername",
> >     "password": "AHardPassword1232"   
> > }
> > ```
> > 
> > > **Response:**
> > > 
> > > ```json
> > > {
> > >   "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MzAzMDMxNSwiaWF0IjoxNjQ1MjU0MzE1LCJqdGkiOiJhODU4YTIzMzcwOTY0ZmY0YTFhOTcyNWFkYmQwZDJlMyIsInVzZXJfaWQiOjUsInVzZXJuYW1lIjoiQVVuaXF1ZVVzZXJuYW1lT2ZNZWRpY2FsU2hvcE93bmVyIiwiZW1haWwiOiJleGFtcGxlMkBlbWFpbC5jb20ifQ.aIrNRfzvFvMiC582VebHnknBGP9MxgwSgdeG8IsRxmM",
> > >   "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1MjU2MTE1LCJpYXQiOjE2NDUyNTQzMTUsImp0aSI6ImE0NjQzOGRmNjY1MjRhODQ4NDk0NzI5ZWI4N2Q4OWJjIiwidXNlcl9pZCI6NSwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5hbWVPZk1lZGljYWxTaG9wT3duZXIiLCJlbWFpbCI6ImV4YW1wbGUyQGVtYWlsLmNvbSJ9.o5zxI4AYZlXX0iLhQLKjoz-t28wOz2_7UspDGn5IOUk"
> > > }
> > > ```
> > > 
> > > **Note:** *Keep these values at some safe section of your application. Breach of any one of them can lead to serious damage.*
> 
> **401 Unauthorized** for unauthenticated login request.
> 
> > ```json
> > {
> >   "detail": "No active account found with the given credentials"
> > }
> > ```

___

**To check if Token is Valid?**

> Use `token/verify` endpoint.
> 
> > Perform a post request on this endpoint and expect for **200 OK** response. If response is **401 Unauthorized** then unauthenticate the user and drag him down to login page.
> > 
> > **Example Request Body:**
> > 
> > ```json
> > {
> >     "token": "any token, it could be access or refresh"
> > }
> > ```

____

### Refresh the tokens

The access token comes with expiration period, i.e. 30 min in our case. So frontend needs to check if the access token is expired or not. 

The access and refresh tokens comes with a payload which contains, `token_type`, it's `expiry period` , `period at which it is assigned`, and many more check below, 

```json
{
  "token_type": "access",
  "exp": 1645256115,
  "iat": 1645254315,
  "jti": "a46438df66524a848494729eb87d89bc",
  "user_id": 5,
  "username": "AUniqueUsernameOfMedicalShopOwner",
  "email": "example2@email.com"
}
```

The frontend program should decrypt the access token everytime if it reached it's expiration period. If that's the case, then backend server won't entertain any new request from the user. 

In this case frontend application have to perform a refresh request at the backend.

**Step 1:** Check if access token is valid or not?

**Step 2:** If no, then check if refresh token is valid or not?

**Step 3:** Most probably refresh token is valid if user have perfromed a login request within 90 days. 

> Perform a `POST` request at `token/refresh/` endpoint with refresh token you got above.
> 
> **Example:**
> 
> ```json
> {
>     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MzAzMDMxNSwiaWF0IjoxNjQ1MjU0MzE1LCJqdGkiOiJhODU4YTIzMzcwOTY0ZmY0YTFhOTcyNWFkYmQwZDJlMyIsInVzZXJfaWQiOjUsInVzZXJuYW1lIjoiQVVuaXF1ZVVzZXJuYW1lT2ZNZWRpY2FsU2hvcE93bmVyIiwiZW1haWwiOiJleGFtcGxlMkBlbWFpbC5jb20ifQ.aIrNRfzvFvMiC582VebHnknBGP9MxgwSgdeG8IsRxmM"
> }
> ```
> 
> > **Response:**
> > 
> > ```json
> > {
> >   "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1MjU3NzIwLCJpYXQiOjE2NDUyNTQzMTUsImp0aSI6ImI4NDZlMzI3NWJlNTQxNTQ5ZTIxNjBiMDUwMDA4NjZkIiwidXNlcl9pZCI6NSwidXNlcm5hbWUiOiJBVW5pcXVlVXNlcm5hbWVPZk1lZGljYWxTaG9wT3duZXIiLCJlbWFpbCI6ImV4YW1wbGUyQGVtYWlsLmNvbSJ9.V0dMf8ChXs7yTJB8xxeeVnW6-P4aRgMFihgnVhFHI6Q",
> >   "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MzAzMTkyMCwiaWF0IjoxNjQ1MjU1OTIwLCJqdGkiOiI0OTgyYWI5YjI4NTg0MWFjYTE2YTZiNWQwOWFkMjA1NSIsInVzZXJfaWQiOjUsInVzZXJuYW1lIjoiQVVuaXF1ZVVzZXJuYW1lT2ZNZWRpY2FsU2hvcE93bmVyIiwiZW1haWwiOiJleGFtcGxlMkBlbWFpbC5jb20ifQ.yEY4sZyxxtwl3crP5jAcPsg9XSIcRf7rqeQZ_lwfoNs"
> > }
> > ```
> > 
> > **Why new refresh token?**
> > 
> > > *Once you perform a refresh request the previous refresh token won't work anymore, this has been done to make these authentication functions more secure.*
> > > 
> > > **So don't forget to update the stored refresh token and access token.**

**Step 4:** If refresh token is expired, then that means user haven't logged In into your application for 90 days. Show him the login page for new tokens.
