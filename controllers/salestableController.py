from fastapi import HTTPException
from models.salestable import SalesTable
from fastapi.responses import JSONResponse
import shutil
from string import ascii_letters
import random

def get_all_salestable(db): 
    salestables = db.query(SalesTable).all()
    return salestables


def get_one_salestable(salestable_id,db): 
    salestable_exist = db.query(SalesTable).filter(SalesTable.id == salestable_id).first()
    if salestable_exist is None:
        raise HTTPException(detail="salestable not found with this id", status_code=404)
    return {
        "salestable_exist":salestable_exist,
        }


def create_salestable(salestable,db):
    salestable = SalesTable(
        movie_name = salestable.movie_name,
        director = salestable.director,
        image = salestable.image,
        price = salestable.price,
        last_update = salestable.last_update
    )
    db.add(salestable)
    db.commit()
    db.refresh(salestable)
    return salestable

def uploadfile(file):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f"_{rand_str}.".join(file.filename.rsplit(".",1))
    path_file = f"uploads/salestable/{new_name}"
    with open(path_file, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"path_file":path_file}

def update_salestable(salestable_id,salestable,db):
    salestable_exist = db.query(SalesTable).filter(SalesTable.id == salestable_id).first()
    if salestable_exist is None:
        raise HTTPException(detail="salestable not found with this id", status_code=404)
    salestable_data = {
        SalesTable.movie_name: salestable.movie_name,
        SalesTable.director: salestable.director,
        SalesTable.image: salestable.image,
        SalesTable.price: salestable.price,
        SalesTable.last_update: salestable.last_update,
    }
    db.query(SalesTable).filter(SalesTable.id == salestable_id).update(salestable_data)
    db.commit()
    return JSONResponse(content="salestable successfully updated")


def delete_salestable(salestable_id,db):
    salestable_exist = db.query(SalesTable).filter(SalesTable.id == salestable_id).first()
    if salestable_exist is None:
        raise HTTPException(detail="salestable not found with this id", status_code=404)
    db.delete(salestable_exist)
    db.commit()
    return JSONResponse(content="salestable successfully deleted  ")