from pydantic import BaseModel, Field
from typing import Optional


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str = Field(
        default=None, title="Password must have Minimum eight characters, at least one letter, one number and one special character", min_length=8, regex="^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    )
    city: str = Field(default="")
    mobile: str = Field(default="")
    designation: str = Field(default="")
    organisation: str = Field(default="")
    role: str = Field(
        default="user", title="admin or user, default value is user"
    )


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Login(BaseModel):
    email: str
    password: str

class Headers(BaseModel):
    Authorization : str

class UserUpdate(UserBase):
    city: Optional[str]
    mobile: Optional[str]
    designation: Optional[str]
    organisation: Optional[str]
    role: Optional[str]

