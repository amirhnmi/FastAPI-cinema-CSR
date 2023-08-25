from dependencies.database import Base
from sqlalchemy import Column,String,Integer,VARCHAR


class News(Base):
    __tablename__="news"

    id = Column(Integer, primary_key=True)
    title = Column(String(length=100))
    image = Column(String(length=250))
    description = Column(String(length=1000))
    news_text = Column(String(length=1000))
    author = Column(String(length=100))
    news_date = Column(String(length=100))
    publish_date = Column(String(length=100)) 