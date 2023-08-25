from fastapi import APIRouter,UploadFile,File
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas import news as schemas
from dependencies.get_db import get_db
from controllers import newsController

router = APIRouter(prefix="/api")

@router.get("/news", response_model=list[schemas.NewsOut])
async def get_all_news(db:Session = Depends(get_db)): 
    return newsController.get_all_news(db)

@router.get("/news/{news_id}")
async def get_one_news(news_id:int, db:Session = Depends(get_db)): 
    return newsController.get_one_news(news_id,db)

@router.post("/news", response_model=schemas.NewsOut)
async def create_news(news:schemas.NewsCreate, db: Session = Depends(get_db)):
    return newsController.create_news(news,db)

@router.post("/news/upload")
def upload_file(file:UploadFile=File(...)):
    return newsController.uploadfile(file)

@router.put("/news/{news_id}")
async def update_news(news_id:int,news:schemas.NewsCreate, db:Session = Depends(get_db)):
    return newsController.update_news(news_id,news,db)

@router.delete("/news/{news_id}")
async def delete_news(news_id:int, db:Session = Depends(get_db)):
    return newsController.delete_news(news_id,db)