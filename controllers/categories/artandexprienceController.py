from fastapi import HTTPException
from models.categories import ArtAndExprience
from fastapi.responses import JSONResponse
import shutil
from string import ascii_letters
import random

def get_all_artandexprience(db): 
    artandexpriences = db.query(ArtAndExprience).all()
    return artandexpriences


def get_one_artandexprience(artandexprience_id,db): 
    artandexprience_exist = db.query(ArtAndExprience).filter(ArtAndExprience.id == artandexprience_id).first()
    if artandexprience_exist is None:
        raise HTTPException(detail="artandexprience not found with this id", status_code=404)
    return {
        "artandexprience_exist":artandexprience_exist,
        }

def create_artandexprience(artandexprience,db):
    artandexprience = ArtAndExprience(
        movie_name = artandexprience.movie_name,
        title = artandexprience.title,
        director = artandexprience.director,
        image = artandexprience.image,
        description = artandexprience.description,
        actors = artandexprience.actors,
        producer = artandexprience.producer,
        production_date = artandexprience.production_date,
        release_date = artandexprience.release_date,
    )
    db.add(artandexprience)
    db.commit()
    db.refresh(artandexprience)
    return artandexprience

def uploadfile(file):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f"_{rand_str}.".join(file.filename.rsplit(".",1))
    path_file = f"uploads/artandexprience/{new_name}"
    with open(path_file, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"path_file":path_file}


def update_artandexprience(artandexprience_id,artandexprience,db):
    artandexprience_exist = db.query(ArtAndExprience).filter(ArtAndExprience.id == artandexprience_id).first()
    if artandexprience_exist is None:
        raise HTTPException(detail="artandexprience not found with this id", status_code=404)
    artandexprience_data = {
        ArtAndExprience.movie_name: artandexprience.movie_name,
        ArtAndExprience.director: artandexprience.director,
        ArtAndExprience.image: artandexprience.image,
        ArtAndExprience.description: artandexprience.description,
        ArtAndExprience.actors: artandexprience.actors,
        ArtAndExprience.producer: artandexprience.producer,
        ArtAndExprience.production_date: artandexprience.production_date,
        ArtAndExprience.release_date: artandexprience.release_date,
    }
    db.query(ArtAndExprience).filter(ArtAndExprience.id == artandexprience_id).update(artandexprience_data)
    db.commit()
    return JSONResponse(content="artandexprience successfully updated")


def delete_artandexprience(artandexprience_id,db):
    artandexprience_exist = db.query(ArtAndExprience).filter(ArtAndExprience.id == artandexprience_id).first()
    if artandexprience_exist is None:
        raise HTTPException(detail="artandexprience not found with this id", status_code=404)
    db.delete(artandexprience_exist)
    db.commit()
    return JSONResponse(content="artandexprience successfully deleted  ")