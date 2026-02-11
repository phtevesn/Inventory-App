from fastapi import APIRouter, Depends, HTTPException, status, Response 
from sqlalchemy.orm import Session 

from schemas import ItemInfo, ItemEdit
from models import Items, Users

from db import get_db
from services.item_service import (
  create_item,
  edit_item,
  delete_item,
  get_items,
  get_child_items,
)
from services.auth_service import get_current_user

router = APIRouter()

@router.post("/item")
def createItem(item_info: ItemInfo, cur_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  new_item = create_item(item_info, cur_user.userid, db)
  if not new_item:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail="Failed to create item"
    )
  return new_item
  
@router.put("/item/{item_id}")
def editItem(item_id: int, item_edit: ItemEdit, db: Session = Depends(get_db)):
  edited_item = edit_item(item_id, item_edit, db)
  if not edited_item:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Failed to edit item"
    )
  return edited_item 

@router.delete("/item/{item_id}")
def deleteItem(item_id: int, db: Session = Depends(get_db)):
  is_deleted = delete_item(item_id, db)
  if not is_deleted:
    raise HTTPException(
      status_code = status.HTTP_404_NOT_FOUND,
      detail="Failed to delete item"
    )
  return True
  
@router.get("/skeleinstance/{skele_instance_id}/item")
def getItems(skele_instance_id: int, db: Session = Depends(get_db)):
  items = get_items(skele_instance_id, db)
  return items

@router.get("/item/{item_id}/children")
def getChildItems(item_id: int, db: Session = Depends(get_db)):
  return get_child_items(item_id, db)
  

