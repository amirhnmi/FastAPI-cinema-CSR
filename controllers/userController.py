from fastapi import HTTPException
from models import users as models
from dependencies.hash import Hash
from fastapi.responses import JSONResponse
hash = Hash()



def get_all_user(db): 
    users = db.query(models.User).all()
    return users


def get_one_user(user_id,db): 
    user_exist = db.query(models.User).filter(models.User.id == user_id).first()
    if user_exist is None:
        raise HTTPException(detail="User not found with this id", status_code=404)
    return {
        "user_exist":user_exist,
        }


def create_user(user,db):
    email_exist = db.query(models.User).filter(models.User.email == user.email).first()
    if email_exist:
        raise HTTPException(detail="Email already exist", status_code=400)
    user = models.User(
        email=user.email,
        username=user.username,
        phone_number=user.phone_number,
        password=hash.bcrypt(user.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(user_id,user,db):
    user_exist = db.query(models.User).filter(models.User.id == user_id).first()
    if user_exist is None:
        raise HTTPException(detail="User not found with this id", status_code=404)
    user_data = {
        models.User.email: user.email,
        models.User.username: user.username,
        models.User.phone_number: user.phone_number,
        models.User.password: hash.bcrypt(user.password),
    }
    db.query(models.User).filter(models.User.id == user_id).update(user_data)
    db.commit()
    return JSONResponse(content="user successfully updated")


def delete_user(user_id,db):
    user_exist = db.query(models.User).filter(models.User.id == user_id).first()
    if user_exist is None:
        raise HTTPException(detail="User not found with this id", status_code=404)
    db.delete(user_exist)
    db.commit()
    return JSONResponse(content="user successfully deleted  ")