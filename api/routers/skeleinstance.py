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

@router.delete("/instance/delete")

@router.get("/instances/get")