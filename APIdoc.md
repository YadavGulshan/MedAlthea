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
> >     "username": "gulshan69"
> > }
> > ```
> 
> 
> 
> 


