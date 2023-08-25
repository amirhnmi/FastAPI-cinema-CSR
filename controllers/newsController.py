from fastapi import HTTPException
from models.news import News
from fastapi.responses import JSONResponse
import shutil
from string import ascii_letters
import random



def get_all_news(db): 
    news = db.query(News).all()
    return news


def get_one_news(news_id,db): 
    news_exist = db.query(News).filter(News.id == news_id).first()
    if news_exist is None:
        raise HTTPException(detail="news not found with this id", status_code=404)
    return {
        "news_exist":news_exist,
        }

def create_news(news,db):
    news = News(
        title = news.title,
        description = news.description,
        image = news.image,
        news_text = news.news_text,
        author = news.author,
        news_date = news.news_date,
        publish_date = news.publish_date,
    )
    db.add(news)
    db.commit()
    db.refresh(news)
    return news

def uploadfile(file):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f"_{rand_str}.".join(file.filename.rsplit(".",1))
    path_file = f"uploads/news/{new_name}"
    with open(path_file, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"path_file":path_file}


def update_news(news_id,news,db):
    news_exist = db.query(News).filter(News.id == news_id).first()
    if news_exist is None:
        raise HTTPException(detail="news not found with this id", status_code=404)
    news_data = {
        News.title: news.title,
        News.description: news.description,
        News.image: news.image,
        News.news_text: news.news_text,
        News.author: news.author,
        News.news_date: news.news_date,
        News.publish_date: news.publish_date,
    }
    db.query(News).filter(News.id == news_id).update(news_data)
    db.commit()
    return JSONResponse(content="news successfully updated")


def delete_news(news_id,db):
    news_exist = db.query(News).filter(News.id == news_id).first()
    if news_exist is None:
        raise HTTPException(detail="news not found with this id", status_code=404)
    db.delete(news_exist)
    db.commit()
    return JSONResponse(content="news successfully deleted  ")