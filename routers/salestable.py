from fastapi import APIRouter,UploadFile,File
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import salestable as schemas
from dependencies.get_db import get_db
from controllers import salestableController


router = APIRouter(prefix="/api")

@router.get("/salestable", response_model=list[schemas.SalesTableOut])
def get_all_salestable(db:Session = Depends(get_db)): 
    return salestableController.get_all_salestable(db)

@router.get("/salestable/{salestable_id}")
def get_one_salestable(salestable_id:int, db:Session = Depends(get_db)): 
    return salestableController.get_one_salestable(salestable_id,db)

@router.post("/salestable", response_model=schemas.SalesTableOut)
def create_salestable(salestable:schemas.SalesTableCreate, db: Session = Depends(get_db)):
    return salestableController.create_salestable(salestable,db,)

@router.post("/salestable/upload")
def upload_file(file:UploadFile=File(...)):
    return salestableController.uploadfile(file)

@router.put("/salestable/{salestable_id}")
def update_salestable(salestable_id:int,salestable:schemas.SalesTableCreate, db:Session = Depends(get_db)):
    return salestableController.update_salestable(salestable_id,salestable,db)

@router.delete("/salestable/{salestable_id}")
def delete_salestable(salestable_id:int, db:Session = Depends(get_db)):
    return salestableController.delete_salestable(salestable_id,db)