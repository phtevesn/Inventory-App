from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Inventories, UserInvs
from schemas import CreateInv

OWNER = 1

def create_inv(id: int, inv_name: str,  db: Session):
  inv = Inventories(
    invname = inv_name, 
    ownerid = id
  )
  try:
    db.add(inv)
    db.flush()
    ownerInv = UserInvs(
      userid = id,
      invid = inv.invid,
      roleid = OWNER
    )
    db.add(ownerInv)
    db.commit()
    db.refresh(inv)
    return inv.invid
  except SQLAlchemyError:
    db.rollback()
    return None

def delete_inv(inv_id: int, id: int, db: Session):
  inv = db.query(Inventories).filter(Inventories.invid == inv_id).first()
  if not inv:
    return "fail"
  if inv.ownerid != id:
    return "unauthorized"
  try:
    db.delete(inv)
    db.commit()
    return "success"
  except SQLAlchemyError:
    db.rollback()
    return "fail"
  
  
def get_invs(id: int, db: Session):
  rows = (
    db.query(Inventories.invid, Inventories.invname)
    .join(UserInvs, UserInvs.invid == Inventories.invid)
    .filter(UserInvs.userid == id)
    .all()
  )
  #okay i need to figure out a way to map rows 

  
  