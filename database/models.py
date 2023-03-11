from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    mobile = Column(String, unique=False)
    city = Column(String, unique=False)
    designation = Column(String, unique=False)
    organisation = Column(String, unique=False)
    role = Column(String, unique=False)
    is_active = Column(Boolean, default=True)