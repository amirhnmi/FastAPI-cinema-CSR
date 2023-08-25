from fastapi import HTTPException
from models.categories import Theater
from fastapi.responses import JSONResponse
import shutil
from string import ascii_letters
import random


def get_all_theater(db): 
    theaters = db.query(Theater).all()
    return theaters


def get_one_theater(theater_id,db): 
    theater_exist = db.query(Theater).filter(Theater.id == theater_id).first()
    if theater_exist is None:
        raise HTTPException(detail="theater not found with this id", status_code=404)
    return {
        "theater_exist":theater_exist,
        }

def create_theater(theater,db):
    theater = Theater(
        movie_name = theater.movie_name,
        title = theater.title,
        director = theater.director,
        image = theater.image,
        description = theater.description,
        actors = theater.actors,
        producer = theater.producer,
        production_date = theater.production_date,
        release_date = theater.release_date,
    )
    db.add(theater)
    db.commit()
    db.refresh(theater)
    return theater

def uploadfile(file):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f"_{rand_str}.".join(file.filename.rsplit(".",1))
    path_file = f"uploads/theater/{new_name}"
    with open(path_file, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"path_file":path_file}


def update_theater(theater_id,theater,db):
    theater_exist = db.query(Theater).filter(Theater.id == theater_id).first()
    if theater_exist is None:
        raise HTTPException(detail="theater not found with this id", status_code=404)
    theater_data = {
        Theater.movie_name: theater.movie_name,
        Theater.director: theater.director,
        Theater.image: theater.image,
        Theater.description: theater.description,
        Theater.actors: theater.actors,
        Theater.producer: theater.producer,
        Theater.production_date: theater.production_date,
        Theater.release_date: theater.release_date,
    }
    db.query(Theater).filter(Theater.id == theater_id).update(theater_data)
    db.commit()
    return JSONResponse(content="theater successfully updated")


def delete_theater(theater_id,db):
    theater_exist = db.query(Theater).filter(Theater.id == theater_id).first()
    if theater_exist is None:
        raise HTTPException(detail="theater not found with this id", status_code=404)
    db.delete(theater_exist)
    db.commit()
    return JSONResponse(content="theater successfully deleted  ")