from fastapi import APIRouter,Depends,HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from datetime import datetime,timedelta
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from dependencies.get_db import get_db
from dependencies.hash import Hash
from models import users as models
from schemas import auth as schemas
from dependencies.exception import EmailNotValid
# forget password
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig


hash = Hash()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "a4ccf8e58dcc5ebc6ce1637d362c2ced20f4dcc030a3e985c97d7f9dfbe29616"  # openssl rand -hex 32
ALGORITHM = "HS256"
token_EXPIRE_MINUTES = 30

def create_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

conf = ConnectionConfig(
    MAIL_USERNAME = "mr.arhnmi@gmail.com",
    MAIL_PASSWORD = "ncxywemnbtswysad",
    MAIL_FROM = "mr.arhnmi@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="arhnmi",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)
router = APIRouter(prefix="/api/auth")

@router.post("/register")
def register(request:schemas.UserRegister, db: Session = Depends(get_db)):
    email_exist = db.query(models.User).filter(models.User.email == request.email).first()
    if email_exist:
        raise HTTPException(detail="Email already exist", status_code=400)
    if "@" not in request.email:
        raise EmailNotValid("email is not valid")
    user = models.User(
        email=request.email,
        username=request.username,
        phone_number=request.phone_number,
        password=hash.bcrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login")
def login(request:schemas.UserLogin, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(detail="invalid email or not found", status_code=404)
    
    if not hash.verify(user.password, request.password):
        raise HTTPException(detail="invalid password", status_code=404)
    

    token = create_token(data={"sub":user.email}) 
    return {
        "token": token,
        "type_token": "bearer",
        "user_id": user.id,
        "username": user.username
    }


@router.post("/usertoken", response_model=schemas.UserOut)
def get_current_user(request:schemas.Token, db:Session=Depends(get_db)):
    error_credential = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid credential",
        headers={"WWW-authenticate":"bearer"})
    try:
        _dict = jwt.decode(request.token, SECRET_KEY, algorithms=ALGORITHM)
        email = _dict.get("sub")
        if not email:
            raise error_credential
    except JWTError:
        raise error_credential
        
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise HTTPException(detail="User not found with this email", status_code=404)
    return user



@router.post("/forget_password")
async def forget_password(request:schemas.ForgetPassword):
    token = create_token(data={"sub":request.email})
    message = MessageSchema(
        subject="cinematicket support",
        recipients=[request.email],  # List of recipients, as many as you can pass
        body=f'Please click the following link to reset your password: http://127.0.0.1:3000/auth/login/reset_password/{token}',
        subtype="html"
        )
 
    fm = FastMail(conf)
    await fm.send_message(message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})



@router.post("/reset_password")
def reset_password(request:schemas.ResetPassword, db:Session=Depends(get_db)):
    error_credential = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid credential",
        headers={"WWW-authenticate":"bearer"})
    try:
        _dict = jwt.decode(request.token, SECRET_KEY, algorithms=ALGORITHM)
        email = _dict.get("sub")
        if not email:
            raise HTTPException(detail="email invalid")
    except JWTError:
        raise error_credential
        
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise HTTPException(detail="User not found with this email", status_code=404)
    
    user_data = {models.User.password: hash.bcrypt(request.password)}
    db.query(models.User).filter(models.User.id == user.id).update(user_data)
    db.commit()
    return JSONResponse(content="user password successfully updated")