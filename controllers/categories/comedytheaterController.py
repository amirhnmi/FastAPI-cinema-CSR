from fastapi import HTTPException
from models.categories import ComedyTheater
from fastapi.responses import JSONResponse
import shutil
from string import ascii_letters
import random

def get_all_comedytheater(db): 
    comedytheaters = db.query(ComedyTheater).all()
    return comedytheaters


def get_one_comedytheater(comedytheaters_id,db): 
    comedytheaters_exist = db.query(ComedyTheater).filter(ComedyTheater.id == comedytheaters_id).first()
    if comedytheaters_exist is None:
        raise HTTPException(detail="comedytheaters not found with this id", status_code=404)
    return {
        "comedytheaters_exist":comedytheaters_exist,
        }

def create_comedytheater(comedytheaters,db):
    comedytheaters = ComedyTheater(
        movie_name = comedytheaters.movie_name,
        title = comedytheaters.title,
        director = comedytheaters.director,
        image = comedytheaters.image,
        description = comedytheaters.description,
        actors = comedytheaters.actors,
        producer = comedytheaters.producer,
        production_date = comedytheaters.production_date,
        release_date = comedytheaters.release_date,
    )
    db.add(comedytheaters)
    db.commit()
    db.refresh(comedytheaters)
    return comedytheaters

def uploadfile(file):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f"_{rand_str}.".join(file.filename.rsplit(".",1))
    path_file = f"uploads/comedytheater/{new_name}"
    with open(path_file, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"path_file":path_file}

def update_comedytheater(comedytheaters_id,comedytheaters,db):
    comedytheaters_exist = db.query(ComedyTheater).filter(ComedyTheater.id == comedytheaters_id).first()
    if comedytheaters_exist is None:
        raise HTTPException(detail="comedytheaters not found with this id", status_code=404)
    comedytheaters_data = {
        ComedyTheater.movie_name: comedytheaters.movie_name,
        ComedyTheater.director: comedytheaters.director,
        ComedyTheater.image: comedytheaters.image,
        ComedyTheater.description: comedytheaters.description,
        ComedyTheater.actors: comedytheaters.actors,
        ComedyTheater.producer: comedytheaters.producer,
        ComedyTheater.production_date: comedytheaters.production_date,
        ComedyTheater.release_date: comedytheaters.release_date,
    }
    db.query(ComedyTheater).filter(ComedyTheater.id == comedytheaters_id).update(comedytheaters_data)
    db.commit()
    return JSONResponse(content="comedytheaters successfully updated")


def delete_comedytheater(comedytheaters_id,db):
    comedytheaters_exist = db.query(ComedyTheater).filter(ComedyTheater.id == comedytheaters_id).first()
    if comedytheaters_exist is None:
        raise HTTPException(detail="comedytheaters not found with this id", status_code=404)
    db.delete(comedytheaters_exist)
    db.commit()
    return JSONResponse(content="comedytheaters successfully deleted  ")