
# W Ventures - User Service

This API service is created to serve third-party entities to use our platform services 


## Features

This API service is protected by API Key authorization
- Sign up
- LogIn
- Update User profile


## Technologies

Python3 , FastAPI, SQLite3, SQLAlchemy(ORM)

## API Security
- **API Key** to restrict access to non reigstered third-party entities
- **JWT token** based authentication with an expiry of 15min
- **RBAC**(Role Based Access Control) to restirct access at user role level
- **md5 Hashed** password is stored in DB
- API Key and Secret Key are stored in environment variables to restrict non-programatic access

## Run Locally

Create virtual environment (name of vitual environment is `myenv`)
```bash
  python3 -m venv myenv
```

Activate the virtual environment
```bash
  source myenv/bin/activate
```

Install dependancies in the myenv
```bash
  pip3 install -r requirements.txt
```

Start the server
```bash
  uvicorn main:app --reload
```

To deactivate the virtual environment
```bash
  deactivate
```

Go to [http://localhost:8000/docs](http://localhost:8000/docs) to open API documentation and test the application 

**NOTE:** All the APIs are protected by API Key (32 bit encoded key) which is unique for each client (third-party entity) . And a 32 Secret key is used for generate and verify JWT tokens 

For local testing use the API key 
```bash
  b5d47de3-d906-45a0-a863-8d93cae2f156
```




## APIs

### Sign up API
(New users will Sign up)
- Email of user is mandatory
- Role of user is mandatory (admin/user)
- Password must have Minimum eight characters, at least one letter, one number and one special character
- Only one registration is allowed for one email id
- If role is not given, it takes `user` as default role
### Login API
(Existing users should Login)
- Only regustered(Signed) users can login. 
- This API returns a JWT token on successful login.
- Token comes with an expiry of 15min
### Update User profile API
(Logged in user can update his profile. admin can update any one's profile in his organization with same api key)
- To update a user profile, one must be logged in and use the **JWT Token** received on successful login.
- Token must be valid (not expired) while hitting this API
- A Logged in user can update only his profile
- Admins can update any user's profile or role
- email is a mandatory field
- password cannot be updated, role cannot be updated by non-admin users
- one or more details like city, organization, designation, mobile can be updated


## Areas of Improvement

- Can incorporate 2 Factor Authentication for users to login along with JWT Token based authentication to improve security
- Can use OKTA/AWS Cognito to manage user profiles and user session 
- Can use Casbin or Okta's user groups to bring in RBAC (since the current scope is limited to profile update alone - RBAC is not implemented)