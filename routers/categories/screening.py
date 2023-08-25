from fastapi import APIRouter,UploadFile,File
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import categories as schemas
from dependencies.get_db import get_db
from controllers.categories import screeningController

router = APIRouter(prefix="/api")

@router.get("/screening", response_model=list[schemas.CategoryOut])
async def get_all_screening(db:Session = Depends(get_db)): 
    return screeningController.get_all_screening(db)

@router.get("/screening/{screening_id}")
async def get_one_screening(screening_id:int, db:Session = Depends(get_db)): 
    return screeningController.get_one_screening(screening_id,db)

@router.post("/screening", response_model=schemas.CategoryOut)
async def create_screening(screening:schemas.CategoryCreate, db: Session = Depends(get_db)):
    return screeningController.create_screening(screening,db)

@router.post("/screening/upload")
def upload_file(file:UploadFile=File(...)):
    return screeningController.uploadfile(file)

@router.put("/screening/{screening_id}")
async def update_screening(screening_id:int,screening:schemas.CategoryCreate, db:Session = Depends(get_db)):
    return screeningController.update_screening(screening_id,screening,db)

@router.delete("/screening/{screening_id}")
async def delete_screening(screening_id:int, db:Session = Depends(get_db)):
    return screeningController.delete_screening(screening_id,db)