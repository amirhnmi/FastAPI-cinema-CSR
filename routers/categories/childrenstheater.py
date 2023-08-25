from fastapi import APIRouter,UploadFile,File
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import categories as schemas
from dependencies.get_db import get_db
from controllers.categories import childrenstheaterController

router = APIRouter(prefix="/api")

@router.get("/childrenstheater", response_model=list[schemas.CategoryOut])
async def get_all_childrenstheater(db:Session = Depends(get_db)): 
    return childrenstheaterController.get_all_childrenstheater(db)

@router.get("/childrenstheater/{childrenstheater_id}")
async def get_one_childrenstheater(childrenstheater_id:int, db:Session = Depends(get_db)): 
    return childrenstheaterController.get_one_childrenstheater(childrenstheater_id,db)

@router.post("/childrenstheater", response_model=schemas.CategoryOut)
async def create_childrenstheater(childrenstheater:schemas.CategoryCreate, db: Session = Depends(get_db)):
    return childrenstheaterController.create_childrenstheater(childrenstheater,db)

@router.post("/childrenstheater/upload")
def upload_file(file:UploadFile=File(...)):
    return childrenstheaterController.uploadfile(file)

@router.put("/childrenstheater/{childrenstheater_id}")
async def update_childrenstheater(childrenstheater_id:int,childrenstheater:schemas.CategoryCreate, db:Session = Depends(get_db)):
    return childrenstheaterController.update_childrenstheater(childrenstheater_id,childrenstheater,db)

@router.delete("/childrenstheater/{childrenstheater_id}")
async def delete_childrenstheater(childrenstheater_id:int, db:Session = Depends(get_db)):
    return childrenstheaterController.delete_childrenstheater(childrenstheater_id,db)