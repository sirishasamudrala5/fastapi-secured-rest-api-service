from typing import Union
from fastapi import FastAPI, Depends, Header, HTTPException
import auth
from fastapi.security.api_key import APIKey
import aboutService as about
from database import models,schemas, helpers
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from jwt import create_access_token, verify_token
import hashlib

models.Base.metadata.create_all(bind=engine)


app = FastAPI(title=about.title,
    description=about.description,
    version=about.version,
    contact=about.contact,openapi_tags=about.tags_metadata)


# Open Route
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Lockedown Route
@app.post("/login", tags=["Login"])
async def login(user: schemas.Login, db: Session = Depends(get_db), api_key: APIKey = Depends(auth.get_api_key)):
    db_user = helpers.get_user_by_email(db, email=user.email)
    user_password = hashlib.md5(user.password.encode()).digest()

    if db_user and db_user.hashed_password == user_password:
        token = create_access_token(data={"email": db_user.email, "organisation": db_user.organisation, "designation": db_user.designation, "role": db_user.role, "exp": 1234})
        return {'token': token}
    elif db_user.hashed_password != user_password:
        raise HTTPException(status_code=401, detail="Incorrect Password")
    return {'token': ''}

@app.post("/sign-up", tags=["SignUp"], response_model=schemas.User)
async def sign_up(user: schemas.UserCreate, db: Session = Depends(get_db), api_key: APIKey = Depends(auth.get_api_key)):
    db_user = helpers.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return helpers.create_user(db=db, user=user)


@app.post("/update-profile", tags=["Profile Update"])
async def update_profile(user: schemas.UserUpdate, db: Session = Depends(get_db), headers: str = Depends(schemas.Headers), api_key: APIKey = Depends(auth.get_api_key)):
    decoded_data = verify_token(headers.Authorization)

    if decoded_data and decoded_data['email'] == user.email or decoded_data['role'] == 'admin':
        if  decoded_data['role'] == 'user' and user.role == 'admin' :
            raise HTTPException(status_code=401, detail="Un Authorized to change role")
        res = helpers.update_user(db=db, user=user)
        return {"message": "updated successfully"}
    else:
        raise HTTPException(status_code=401, detail="Un Authorized")