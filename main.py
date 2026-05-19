from fastapi import FastAPI
from pydantic import BaseModel
from database import Base, engine
from database import SessionLocal
from models import Event

Base.metadata.create_all(bind=engine)
app = FastAPI()

events = {}
submissions = {}


@app.get("/api")
def read_root():
    return {"message" : "Hello, FastAPI!"}

@app.get("/api/event/{event_id}")
def signup_to_event():
    return {}


@app.post("")
