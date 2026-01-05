from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Items
from schemas import ItemInfo

def create_item(item_info: ItemInfo, cur_user: int, db: Session):
  item = Items(
    skeleinstanceid = item_info.skele_instance_id,
    parentitemid = item_info.parent_item_id, 
    statusid = item_info.status_id, 
    creatorid = cur_user,
    notes = item_info.notes
  )
  
  try:
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
  except SQLAlchemyError:
    db.rollback()
    return None
    
def edit_item(item_id: int, status_id: int, notes: str, db: Session):
  #change status or notes 
  item = db.query(Items).filter(Items.itemid == item_id).first()
  if not item:
    return None 
  
  item.statusid = status_id
  item.notes = notes
  
  try: 
    db.commit()
    db.refresh(item)
    return item
  except SQLAlchemyError:
    db.rollback()
    return None
  
def delete_item(item_id: int, db: Session):
  item = db.query(Items).filter(Items.itemid == item_id).first()
  if not item: 
    return None
  
  try: 
    db.delete(item)
    db.commit()
    return True
  except:
    db.rollback()
    return None

def get_items(skele_instance_id: int, db: Session):
  items = db.query(Items).filter(Items.skeleinstanceid == skele_instance_id).all()
  return items