# MedAlthea

#### API Urls

> **Note**: *API urls starts with `domain.com/api/`*

**Register User**

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

**Login User**

> **Note:** *After completing the registeration, service program shall perform a login request on behalf of user to get the `access token` and `refresh token`*

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
> > 
> > ```
> > 
> > 
