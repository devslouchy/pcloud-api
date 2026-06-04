from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.database import SessionLocal, engine, get_db
from app.models import Base, Item
from app.db.init_db import wait_for_db


app = FastAPI(
    title="Personal Cloud API",
    version="0.2.1"
)

wait_for_db()

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


@app.post("/items")
def create_item(name: str):
    db: Session = SessionLocal()

    item = Item(name=name)

    db.add(item)
    db.commit()
    db.refresh(item)

    db.close()

    return item


@app.get("/items")
def list_items():
    db: Session = SessionLocal()

    items = db.query(Item).all()

    db.close()

    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    db: Session = SessionLocal()

    item = db.query(Item).filter(
        Item.id == item_id
    ).first()

    db.close()

    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()

    return {"message": "Item deleted"}