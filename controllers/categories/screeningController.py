from fastapi import HTTPException
from models.categories import Screening
from fastapi.responses import JSONResponse
import shutil
from string import ascii_letters
import random


def get_all_screening(db): 
    screenings = db.query(Screening).all()
    return screenings


def get_one_screening(screening_id,db): 
    screening_exist = db.query(Screening).filter(Screening.id == screening_id).first()
    if screening_exist is None:
        raise HTTPException(detail="screening not found with this id", status_code=404)
    return {
        "screening_exist":screening_exist,
        }

def create_screening(screening,db):
    screening = Screening(
        movie_name = screening.movie_name,
        title = screening.title,
        director = screening.director,
        image = screening.image,
        description = screening.description,
        actors = screening.actors,
        producer = screening.producer,
        production_date = screening.production_date,
        release_date = screening.release_date,
    )
    db.add(screening)
    db.commit()
    db.refresh(screening)
    return screening

def uploadfile(file):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f"_{rand_str}.".join(file.filename.rsplit(".",1))
    path_file = f"uploads/screening/{new_name}"
    with open(path_file, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"path_file":path_file}

def update_screening(screening_id,screening,db):
    screening_exist = db.query(Screening).filter(Screening.id == screening_id).first()
    if screening_exist is None:
        raise HTTPException(detail="screening not found with this id", status_code=404)
    screening_data = {
        Screening.movie_name: screening.movie_name,
        Screening.director: screening.director,
        Screening.image: screening.image,
        Screening.description: screening.description,
        Screening.actors: screening.actors,
        Screening.producer: screening.producer,
        Screening.production_date: screening.production_date,
        Screening.release_date: screening.release_date,
    }
    db.query(Screening).filter(Screening.id == screening_id).update(screening_data)
    db.commit()
    return JSONResponse(content="screening successfully updated")


def delete_screening(screening_id,db):
    screening_exist = db.query(Screening).filter(Screening.id == screening_id).first()
    if screening_exist is None:
        raise HTTPException(detail="screening not found with this id", status_code=404)
    db.delete(screening_exist)
    db.commit()
    return JSONResponse(content="screening successfully deleted  ")