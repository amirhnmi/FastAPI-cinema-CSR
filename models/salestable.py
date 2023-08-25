from dependencies.database import Base
from sqlalchemy import Column,String,Integer


class SalesTable(Base):
    __tablename__="salestable"

    id = Column(Integer, primary_key=True)
    movie_name = Column(String(length=100))
    director = Column(String(length=100))
    image = Column(String(length=250))
    price = Column(String(length=100))
    last_update = Column(String(length=100))

