from fastapi import APIRouter,UploadFile,File
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import categories as schemas
from dependencies.get_db import get_db
from controllers.categories import artandexprienceController

router = APIRouter(prefix="/api")

@router.get("/artandexprience", response_model=list[schemas.CategoryOut])
async def get_all_artandexprience(db:Session = Depends(get_db)): 
    return artandexprienceController.get_all_artandexprience(db)

@router.get("/artandexprience/{artandexprience_id}")
async def get_one_artandexprience(artandexprience_id:int, db:Session = Depends(get_db)): 
    return artandexprienceController.get_one_artandexprience(artandexprience_id,db)

@router.post("/artandexprience", response_model=schemas.CategoryOut)
async def create_artandexprience(artandexprience:schemas.CategoryCreate, db: Session = Depends(get_db)):
    return artandexprienceController.create_artandexprience(artandexprience,db)

@router.post("/artandexprience/upload")
def upload_file(file:UploadFile=File(...)):
    return artandexprienceController.uploadfile(file)

@router.put("/artandexprience/{artandexprience_id}")
async def update_artandexprience(artandexprience_id:int,artandexprience:schemas.CategoryCreate, db:Session = Depends(get_db)):
    return artandexprienceController.update_artandexprience(artandexprience_id,artandexprience,db)

@router.delete("/artandexprience/{artandexprience_id}")
async def delete_artandexprience(artandexprience_id:int, db:Session = Depends(get_db)):
    return artandexprienceController.delete_artandexprience(artandexprience_id,db)