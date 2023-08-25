from fastapi import APIRouter,UploadFile,File
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import categories as schemas
from dependencies.get_db import get_db
from controllers.categories import comedytheaterController

router = APIRouter(prefix="/api")

@router.get("/comedytheater", response_model=list[schemas.CategoryOut])
async def get_all_comedytheater(db:Session = Depends(get_db)): 
    return comedytheaterController.get_all_comedytheater(db)

@router.get("/comedytheater/{comedytheater_id}")
async def get_one_comedytheater(comedytheater_id:int, db:Session = Depends(get_db)): 
    return comedytheaterController.get_one_comedytheater(comedytheater_id,db)

@router.post("/comedytheater", response_model=schemas.CategoryOut)
def create_comedytheater(comedytheater:schemas.CategoryCreate, db: Session = Depends(get_db)):
    return comedytheaterController.create_comedytheater(comedytheater,db)

@router.post("/comedytheater/upload")
def upload_file(file:UploadFile=File(...)):
    return comedytheaterController.uploadfile(file)

@router.put("/comedytheater/{comedytheater_id}")
async def update_comedytheater(comedytheater_id:int,comedytheater:schemas.CategoryCreate, db:Session = Depends(get_db)):
    return comedytheaterController.update_comedytheater(comedytheater_id,comedytheater,db)

@router.delete("/comedytheater/{comedytheater_id}")
async def delete_comedytheater(comedytheater_id:int, db:Session = Depends(get_db)):
    return comedytheaterController.delete_comedytheater(comedytheater_id,db)