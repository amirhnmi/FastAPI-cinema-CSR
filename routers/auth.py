from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from dependencies.get_db import get_db
from schemas import auth as schemas
from controllers import authController

router = APIRouter(prefix="/api/auth")

@router.post("/register")
def register(request:schemas.UserRegister, db: Session = Depends(get_db)):
    return authController.register(request,db)

@router.post("/login")
def login(request:schemas.UserLogin, db:Session=Depends(get_db)):
    return authController.login(request,db)

@router.post("/usertoken", response_model=schemas.UserOut)
def get_current_user(request:schemas.Token, db:Session=Depends(get_db)):
    return authController.get_current_user(request,db)

@router.post("/forget_password")
async def forget_password(request:schemas.ForgetPassword):
    return authController.forget_password(request)

@router.post("/reset_password")
def reset_password(request:schemas.ResetPassword, db:Session=Depends(get_db)):
 return authController.reset_password(request,db)