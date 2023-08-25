from fastapi import APIRouter,UploadFile,File
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import categories as schemas
from dependencies.get_db import get_db
from controllers.categories import theaterController

router = APIRouter(prefix="/api")

@router.get("/theater", response_model=list[schemas.CategoryOut])
async def get_all_theater(db:Session = Depends(get_db)): 
    return theaterController.get_all_theater(db)

@router.get("/theater/{theater_id}")
async def get_one_theater(theater_id:int, db:Session = Depends(get_db)): 
    return theaterController.get_one_theater(theater_id,db)

@router.post("/theater", response_model=schemas.CategoryOut)
def create_theater(theater:schemas.CategoryCreate, db: Session = Depends(get_db)):
    return theaterController.create_theater(theater,db)

@router.post("/theater/upload")
def upload_file(file:UploadFile=File(...)):
    return theaterController.uploadfile(file)

@router.put("/theater/{theater_id}")
async def update_theater(theater_id:int,theater:schemas.CategoryCreate, db:Session = Depends(get_db)):
    return theaterController.update_theater(theater_id,theater,db)

@router.delete("/theater/{theater_id}")
async def delete_theater(theater_id:int, db:Session = Depends(get_db)):
    return theaterController.delete_theater(theater_id,db)