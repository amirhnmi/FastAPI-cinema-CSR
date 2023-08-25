from fastapi import UploadFile,File
from pydantic import BaseModel
from typing import Optional

class CategoryCreate(BaseModel):
    movie_name : str
    title : str
    description : str
    image : str
    director : str
    actors : str
    producer : str
    production_date : str
    release_date : str


class CategoryOut(CategoryCreate):
    id : int

    class config:
        orm_mode = True