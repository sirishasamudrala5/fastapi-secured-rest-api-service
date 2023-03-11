from fastapi import FastAPI, status, HTTPException
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta
import config


# Pydantic Model that will be used in the
# token endpoint for the response
class Token(BaseModel):
	access_token: str
	token_type: str


# this function will create the token
# for particular data
def create_access_token(data: dict):
	to_encode = data.copy()
	
	# expire time of the token
	expire = datetime.utcnow() + timedelta(minutes=15)
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
	
	# return the generated token
	return encoded_jwt


def verify_token(token: str):
	try:
		# try to decode the token, it will
		# raise error if the token is not correct
		payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
		return payload
	except JWTError:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Could not validate credentials",
		)
