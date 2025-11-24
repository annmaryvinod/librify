from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.book import BookCreate, BookResponse
from app.services.book_service import (
    create_book, get_books, get_book, delete_book
)
from typing import List

router = APIRouter(prefix="/api/books", tags=["books"])

@router.post("/", response_model=BookResponse, status_code=201)
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.get("/", response_model=List[BookResponse])
def list_books_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_books(db, skip, limit)

@router.get("/{book_id}", response_model=BookResponse)
def get_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}", status_code=204)
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    if not delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return None