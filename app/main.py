from fastapi import FastAPI
from sqlalchemy import text
from app.db.database import SessionLocal, engine, get_db, Base
from app.models import Item
from app.db.init_db import wait_for_db
from app.routers import items


app = FastAPI(
    title="Personal Cloud API",
    version="0.2.1"
)

wait_for_db()

Base.metadata.create_all(bind = engine)
app.include_router(items.router)

@app.on_event("startup")
def startup():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
       
        Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}