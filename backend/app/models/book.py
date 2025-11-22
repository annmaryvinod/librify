from sqlalchemy import Column, Integer, String, Date
from app.config.database import Base #to create the database models

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False)
    language = Column(String, nullable=False)