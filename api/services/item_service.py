from sqlalchemy import delete, select, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Items, ChildItems
from schemas import ItemInfo

def create_item(item_info: ItemInfo, cur_user: int, db: Session):
  item = Items(
    skeleinstanceid = item_info.skele_instance_id,
    statusid = item_info.status_id, 
    creatorid = cur_user,
    notes = item_info.notes
  )
  
  child_items = item_info.item_childs
  parent_item = item_info.item_parent
  
  try:
    db.add(item)
    
    create_child_items(item.itemid, child_items, db)
    set_parent_item(item.itemid, db, parent_item_id = parent_item)
    
    db.commit()
    db.refresh(item)
    return item
  except SQLAlchemyError:
    db.rollback()
    return None
    
def edit_item(item_id: int, status_id: int, parent_id: int, child_items_id: list[int], notes: str, db: Session):
  item = db.query(Items).filter(Items.itemid == item_id).first()
  if not item:
    return None 
  
  item.statusid = status_id
  item.notes = notes
  
  try: 
    create_child_items(item_id, child_items_id, db)
    set_parent_item(item_id, db, parent_item_id=parent_id)
    
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

def create_child_items(item_id: int, child_items: list[int], db: Session):
  try:
    db.execute(
      delete(ChildItems).where(ChildItems.childitemid.in_(child_items))
    )
    
    rows = [{"childitemid": ci, "parentitemid": item_id} for ci in child_items]
    db.execute(insert(ChildItems), rows)
    return True
  except SQLAlchemyError as e:
    db.rollback()
    print(e)
    return False
  
def get_child_items(item_id: int, db: Session):
  return db.scalars(
    select(ChildItems.childitemid).where(ChildItems.parentitemid == item_id)
  ).all()
  
def get_parent_item(item_id: int, db: Session):
  return db.query(ChildItems.parentitemid).filter(ChildItems.childitemid == item_id).first()
  
def set_parent_item(item_id: int, db: Session, parent_item_id = -1):
  #necessary when creating or editing an item where they add a parent item to attach current item to
  try:
    db.execute(
      delete(ChildItems).where(ChildItems.childitemid == item_id)
    )
    if (parent_item_id > 0):
      db.execute(
        insert(ChildItems), {"childitemid": item_id, "parentitemid": parent_item_id}
      )
    return True
  except SQLAlchemyError as e:
    db.rollback()
    print(e)
    return False
  
