from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db, SessionLocal
from app.models import Item

from app.schemas import ItemCreate, ItemResponse

router = APIRouter()

@router.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    new_item = Item(name=item.name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item




@router.get("/items")
def list_items():
    db: Session = SessionLocal()

    items = db.query(Item).all()

    db.close()

    return items


@router.get("/items/{item_id}")
def get_item(item_id: int):
    db: Session = SessionLocal()

    item = db.query(Item).filter(
        Item.id == item_id
    ).first()

    db.close()

    return item

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()

    return {"message": "Item deleted"}
    
    
    
@router.put("/items/{item_id}")
def replace_item(item_id: int, name:str, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
        
    item.name = name
    db.commit()
    db.refresh(item)    
    return {"message": "Item updated"}
