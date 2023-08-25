from pydantic import BaseModel

class UserBase(BaseModel):
    email : str
    username : str
    phone_number : str

class UserCreate(UserBase):
    password : str



class UserOut(UserBase):
    id : int
    isadmin : bool

    class config:
        orm_mode = True