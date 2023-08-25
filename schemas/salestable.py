from pydantic import BaseModel


class SalesTableCreate(BaseModel):
    movie_name : str
    director : str
    image : str
    price : str
    last_update : str


class SalesTableOut(SalesTableCreate):
    id : int

    class config:
        orm_mode = True