from fastapi import HTTPException
from models.categories import ChildrensTheater
from fastapi.responses import JSONResponse
import shutil
from string import ascii_letters
import random

def get_all_childrenstheater(db): 
    childrenstheaters = db.query(ChildrensTheater).all()
    return childrenstheaters


def get_one_childrenstheater(childrenstheater_id,db): 
    childrenstheater_exist = db.query(ChildrensTheater).filter(ChildrensTheater.id == childrenstheater_id).first()
    if childrenstheater_exist is None:
        raise HTTPException(detail="childrenstheater not found with this id", status_code=404)
    return {
        "childrenstheater_exist":childrenstheater_exist,
        }

def create_childrenstheater(childrenstheater,db):
    childrenstheater = ChildrensTheater(
        movie_name = childrenstheater.movie_name,
        title = childrenstheater.title,
        director = childrenstheater.director,
        image = childrenstheater.image,
        description = childrenstheater.description,
        actors = childrenstheater.actors,
        producer = childrenstheater.producer,
        production_date = childrenstheater.production_date,
        release_date = childrenstheater.release_date,
    )
    db.add(childrenstheater)
    db.commit()
    db.refresh(childrenstheater)
    return childrenstheater

def uploadfile(file):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f"_{rand_str}.".join(file.filename.rsplit(".",1))
    path_file = f"uploads/childrenstheater/{new_name}"
    with open(path_file, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"path_file":path_file}

def update_childrenstheater(childrenstheater_id,childrenstheater,db):
    childrenstheater_exist = db.query(ChildrensTheater).filter(ChildrensTheater.id == childrenstheater_id).first()
    if childrenstheater_exist is None:
        raise HTTPException(detail="childrenstheater not found with this id", status_code=404)
    childrenstheater_data = {
        ChildrensTheater.movie_name: childrenstheater.movie_name,
        ChildrensTheater.director: childrenstheater.director,
        ChildrensTheater.image: childrenstheater.image,
        ChildrensTheater.description: childrenstheater.description,
        ChildrensTheater.actors: childrenstheater.actors,
        ChildrensTheater.producer: childrenstheater.producer,
        ChildrensTheater.production_date: childrenstheater.production_date,
        ChildrensTheater.release_date: childrenstheater.release_date,
    }
    db.query(ChildrensTheater).filter(ChildrensTheater.id == childrenstheater_id).update(childrenstheater_data)
    db.commit()
    return JSONResponse(content="childrenstheater successfully updated")


def delete_childrenstheater(childrenstheater_id,db):
    childrenstheater_exist = db.query(ChildrensTheater).filter(ChildrensTheater.id == childrenstheater_id).first()
    if childrenstheater_exist is None:
        raise HTTPException(detail="childrenstheater not found with this id", status_code=404)
    db.delete(childrenstheater_exist)
    db.commit()
    return JSONResponse(content="childrenstheater successfully deleted  ")