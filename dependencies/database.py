from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:manamirhastam@127.0.0.1:3306/cinematicket-fastapi")
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()