from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    language: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        from_attributes = True