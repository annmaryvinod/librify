#imports
from sqlalchemy import create_engine #to connect to the database
from sqlalchemy.ext.declarative import declarative_base #to create the database models
from sqlalchemy.orm import sessionmaker #to create the database session
import os #to get the environment variables
from dotenv import load_dotenv #to load the environment variables

#load the environment variables
load_dotenv()

#get the database url from the environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Please add it to your environment or .env file.")

#create the engine
engine = create_engine(DATABASE_URL)

#create the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#create the base model
Base = declarative_base()

#create the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()