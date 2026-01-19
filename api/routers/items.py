from fastapi import APIRouter, Depends, HTTPException, status, Response 
from sqlalchemy.orm import Session 

from schemas import ItemInfo 
from models import Items, Users

from db import get_db
from services.item_service import (
  create_item,
  edit_item,
  delete_item,
  get_items
)
from services.auth_service import get_current_user

router = APIRouter()


@router.post("/item/create")
def createItem(item_info: ItemInfo, cur_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  new_item = create_item(item_info, cur_user.userid, db)
  if not new_item:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail="Failed to create item"
    )
  return new_item
  
@router.put("/item/edit")
def editItem(item_id: int, status_id: int, notes: str, db: Session = Depends(get_db)):
  edited_item = edit_item(item_id, status_id, notes, db)
  if not edited_item:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Failed to edit item"
    )
  return edited_item 

@router.delete("/item/delete")
def deleteItem(item_id: int, db: Session = Depends(get_db)):
  is_deleted = delete_item(item_id, db)
  if not is_deleted:
    raise HTTPException(
      status_code = status.HTTP_404_NOT_FOUND,
      detail="Failed to edit item"
    )
  return True
  
@router.get("/item/get")
def getItems(skele_instance_id: int, db: Session = Depends(get_db)):
  items = get_items(skele_instance_id, db)
  if not items:
    raise HTTPException(
      status_code = status.HTTP_404_NOT_FOUND, 
      detail = f"Failed to get items with skele instance id {skele_instance_id}"
    )
  return items