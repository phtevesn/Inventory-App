from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Statuses, Users 
from schemas import StatusInfo, StatusInv

from db import get_db 
from services.auth_service import get_current_user
from services.status_service import (
  create_status,
  edit_status,
  delete_status,
  get_inv_statuses,
  get_user_statuses,
  add_inv_status
)

router = APIRouter()

@router.post("/statuses")
def createStatus(status_info: StatusInfo, cur_user = Depends(get_current_user), db: Session = Depends(get_db)):
  cur_status = create_status(status_info, cur_user.userid, db)
  if not cur_status:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail="Failed to create status"
    )
  return cur_status

@router.put("/statuses/{status_id}")
def editStatus(status_id: int, status_info: StatusInfo, db: Session = Depends(get_db)):
  cur_status = edit_status(status_id, status_info, db)
  if not cur_status:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail="Failed to create status"
    )
  return cur_status

@router.delete("/statuses/{status_id}")
def deleteStatus(status_id: int, db: Session = Depends(get_db)):
  if not delete_status(status_id, db):
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail = f"Could not find status with status id: {status_id}"
    )
  return True

@router.get("/inventories/{inv_id}/statuses")
def getInvStatuses(inv_id: int, db:Session = Depends(get_db)):
  statuses = get_inv_statuses(inv_id, db)
  if not statuses:
    raise HTTPException(
      status_code = status.HTTP_404_NOT_FOUND,
      detail=f"Failed to get statuses for inventory with inventory id: {inv_id}"
    )
  return statuses

@router.get("/users/me/statuses")
def getUserStatuses(cur_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  statuses = get_user_statuses(cur_user.userid,db)
  if not statuses:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Could not find statuses for user: {cur_user.username}"
    )
  return statuses

@router.post("/inventories/{inv_id}/statuses")
def addInvStatus(inv_id: int, status_info: StatusInv, db:Session = Depends(get_db)):
  relation = add_inv_status(inv_id, status_info.status_id, db)
  if not relation:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail=f"Failed to add status: {status_info.status_id} to inventory {inv_id}"
    )
  return relation