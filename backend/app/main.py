from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import books

app = FastAPI(title="Librify API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router)

@app.get("/")
def root():
    return {"message": "Librify API is running"}