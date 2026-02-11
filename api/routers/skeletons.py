from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from schemas import SkeleInfo
from models import Users

from db import get_db
from services.skele_service import (
  create_skele, 
  get_user_skeles, 
  delete_skele, 
  edit_skele, 
  get_inv_skeles, 
  favorite_skele, 
  unfavorite_skele,
  get_child_skeles
)
from services.auth_service import get_current_user

router = APIRouter()

@router.post("/skeleton")
def createSkeleton(skele_info: SkeleInfo, cur_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  skele = create_skele(skele_info, cur_user.userid, db) 
  if not skele:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Skeleton was failed to create"
    )
  return {"message": f"Skeleton id:{skele['id']} was created name:{skele['name']}"}

@router.put("/skeleton/{skele_id}")
def editSkeleton(skele_id: int, skele_info: SkeleInfo, db: Session = Depends(get_db)):
  skele = edit_skele(skele_info, skele_id, db)
  if not skele:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail="Skeleton failed to edit"
    )
  return {"message": f"gucci mane"}
  

@router.delete("/skeleton/{skele_id}")
def deleteSkeleton(skele_id: int, cur_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  if not delete_skele(cur_user.userid, skele_id, db):
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail = "Failed to delete skeleton"
    )
  return {"message": "Deleted Skeleton"}    
  

@router.get("/skeleton")
def getUserSkeletons(cur_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  skele = get_user_skeles(cur_user.userid, db)
  return skele


@router.get("/inventory/{inv_id}/skeletons")
def getInvSkeletons(inv_id: int, db: Session = Depends(get_db)):
  skele = get_inv_skeles(inv_id, db)
  return skele

@router.post("/skeleton/{skele_id}/favorite")
def favoriteSkeleton(skele_id: int, cur_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  check = favorite_skele(cur_user.userid, skele_id, db)
  if not check:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST, 
      detail = "Failed to favorite skeleton"
    )
  return True

@router.delete("/skeleton/{skele_id}/favorite")
def unfavoriteSkeleton(skele_id: int, cur_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  check = unfavorite_skele(cur_user.userid, skele_id, db)
  if not check:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail = "Failed to unfavorite skeleton"
    )
  return True

@router.get("/skeleton/{skele_id}")
def childSkeletons(skele_id: int, db: Session = Depends(get_db)):
  childs = get_child_skeles(skele_id, db)
  return childs