from pydantic import EmailStr, BaseModel
from typing import List

class Token(BaseModel):
    token : str

class UserOut(BaseModel):
    id : int
    username : str 
    phone_number : str
    email : str or None = None

class UserRegister(BaseModel):
    email : str
    username : str
    phone_number : str
    password : str

class UserLogin(BaseModel):
    email : str
    password : str

class ForgetPassword(BaseModel):
    email: str

class ResetPassword(BaseModel):
    token : str
    password : str


