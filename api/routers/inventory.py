from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from schemas import CreateInv
from models import Users

from db import get_db
from services.inv_service import create_inv, get_invs, delete_inv
from services.auth_service import get_current_user

router = APIRouter()

@router.post("/inventory/create")
def createInventory(inv_info: CreateInv, current_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  inv_name = inv_info.invName
  
  inv = create_inv(current_user.userid, inv_name, db)
  if not inv:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Inventory was failed to create"
    )
  return {"message": f"Inventory ({inv_name}) created", "inventory_id": inv}
  
@router.get("/inventory/delete")
def deleteInventory(inv_id: int, current_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  res = delete_inv(inv_id, current_user.userid, db)
  if res == "fail":
    raise HTTPException(
      status_code = status.HTTP_404_NOT_FOUND,
      detail = "Could not find inventory"
    )
  elif res == "unauthorized":
    raise HTTPException(
      status_code = status.HTTP_401_UNAUTHORIZED,
      detail = "Not owner of inventory"
    )
  return {"message": "Inventory deleted"}
  
  
@router.get("/inventory/get")
def getInventories(current_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  inventories = get_invs(current_user.userid, db)
  return inventories
  
  
