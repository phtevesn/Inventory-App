from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Users, SkeleInstances
from schemas import SkeleInstanceInfo

from db import get_db
from services.auth_service import get_current_user
from services.skele_ins_service import (
  create_skele_instance,
  edit_skele_instance,
  delete_skele_instance,
  get_skele_instances
)
router = APIRouter()

@router.post("/instance/create")
def createSkeleInstance(instance_info: SkeleInstanceInfo, cur_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  skele_instance = create_skele_instance(instance_info, cur_user.userid, db)
  if not skele_instance:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Failed to create new skeleton instance"
    )
  return skele_instance

@router.put("/instance/edit")
def editSkeleInstance(instance_id: int, folder_id: int, count: int, db: Session = Depends(get_db)):
  skele_instance = edit_skele_instance(instance_id, folder_id, count, db)
  if not skele_instance:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail=f"Failed to edit skele instance with id: {instance_id}"
    )
  return skele_instance
                                       
@router.delete("/instance/delete")
def deleteSkeleInstance(instance_id: int, db: Session = Depends(get_db)):
  if not deleteSkeleInstance(instance_id, db):
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail=f"Failed to delete skele instance with id: {instance_id}"
    )
  return True

@router.get("/instances/get")
def getSkeleInstances(inv_id: int, db:Session = Depends(get_db)):
  instances = get_skele_instances(inv_id, db)
  if not instances:
    raise HTTPException(
      status_code = status.HTTP_404_NOT_FOUND,
      detail = f"No instances for inventory with id: {inv_id}"
    )
  return instances