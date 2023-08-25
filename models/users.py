from dependencies.database import Base
from sqlalchemy import Column,Integer,String,Boolean,BOOLEAN

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(length=100), unique=True, nullable=False)
    username= Column(String(length=100), nullable=False)
    phone_number= Column(String(length=14), nullable=False)
    password= Column(String(length=100), nullable=False)
    isadmin= Column(Boolean, default=False)
