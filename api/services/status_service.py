from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Statuses, InvStatuses
from schemas import StatusInfo

def create_status(status_info: StatusInfo, cur_user: int, db: Session):
  status = Statuses(
    statusname = status_info.status_name,
    imgpath = status_info.img_path,
    doesitcount = status_info.does_it_count,
    creatorid = cur_user
  )

  try:
    db.add(status)
    db.commit()
    db.refresh(status)
    return status
  except SQLAlchemyError:
    db.rollback()
    return None

def edit_status(status_id: int, status_info: StatusInfo, db:Session):
  status = db.query(Statuses).filter(Statuses.statusid == status_id).first()
  if not status:
    return None
  
  status.statusname = status_info.status_name,
  status.imgpath = status_info.img_path,
  status.doesitcount = status_info.does_it_count

  try:
    db.commit()
    db.refresh(status)
    return status
  except SQLAlchemyError:
    db.rollback()
    return None

def delete_status(status_id: int, db:Session):
  status = db.query(Statuses).filter(Statuses.statusid == status_id).first()
  if not status:
    return None
  
  try:
    db.delete(status)
    db.commit()
    return True
  except SQLAlchemyError:
    db.rollback()
    return None


def get_user_statuses(user_id: int, db:Session):
  statuses = db.query(Statuses).filter(Statuses.creatorid == user_id).all()
  return statuses

def get_inv_statuses(inv_id: int, db:Session):
  inv_status_ids = db.query(InvStatuses.statusid).filter(InvStatuses.invid == inv_id).all()
  if not inv_status_ids:
    return None
  status_ids = [status[0] for status in inv_status_ids]
  statuses = db.query(Statuses).filter(Statuses.statusid.in_(status_ids)).all()
  return statuses

def add_inv_status(inv_id: int, status_id: int, db:Session):
  relation = InvStatuses(
    statusid = status_id,
    invid = inv_id
  )
  
  try:
    db.add(relation)
    db.commit()
    db.refresh(relation)
    return relation
  except SQLAlchemyError:
    db.rollback()
    return None
  
  

'''
def get_fav_statuses(cur_user: int, db:Session):

def fav_status(cur_user: int, status_id: int, db:Session):

def unfav_status(cur_user:int, status_id: int, db:Session):
'''