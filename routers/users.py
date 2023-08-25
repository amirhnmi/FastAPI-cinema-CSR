from fastapi import APIRouter
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import users as schemas
from dependencies.get_db import get_db
from controllers import userController

router = APIRouter(prefix="/api")

@router.get("/user", response_model=list[schemas.UserOut])
def get_all_user(db:Session = Depends(get_db)): 
    return userController.get_all_user(db)

@router.get("/user/{user_id}")
def get_one_user(user_id:int, db:Session = Depends(get_db)): 
    return userController.get_one_user(user_id,db)

@router.post("/user", response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    return userController.create_user(user,db)


@router.put("/user/{user_id}")
def update_user(user_id:int,user:schemas.UserCreate, db:Session = Depends(get_db)):
    return userController.update_user(user_id,user,db)

@router.delete("/user/{user_id}")
def delete_user(user_id:int, db:Session = Depends(get_db)):
    return userController.delete_user(user_id,db)

