from dependencies.database import Base
from sqlalchemy import Column,String,Integer

class Category():
    movie_name = Column(String(length=100), nullable=False)
    title = Column(String(length=100), nullable=False)
    description = Column(String(length=1000), nullable=False)
    image = Column(String(length=500), nullable=False)
    director = Column(String(length=100), nullable=False)
    actors = Column(String(length=250), nullable=False)
    producer = Column(String(length=100), nullable=False)
    production_date = Column(String(length=100), nullable=False)
    release_date = Column(String(length=100), nullable=False)

class Theater(Base,Category):
    __tablename__="theaters"
    id = Column(Integer, primary_key=True)

class Screening(Base,Category):
    __tablename__="screenings"
    id = Column(Integer, primary_key=True)

class ArtAndExprience(Base,Category):
    __tablename__="artandexpriences"
    id = Column(Integer, primary_key=True)

class ComedyTheater(Base,Category):
    __tablename__="comedytheaters"
    id = Column(Integer, primary_key=True)

class ChildrensTheater(Base,Category):
    __tablename__="childrenstheaters"
    id = Column(Integer, primary_key=True)
