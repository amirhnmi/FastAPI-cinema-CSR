from pydantic import BaseModel

class NewsCreate(BaseModel):
    title : str
    image : str
    description : str
    news_text : str
    author : str
    news_date : str
    publish_date : str 


class NewsOut(NewsCreate):
    id : int

    class config:
        orm_mode = True