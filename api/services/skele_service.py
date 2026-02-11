from sqlalchemy import func, insert, select, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Skeletons, UserSkelesFav, InvSkeles, ChildSkeles
from schemas import SkeleInfo

def create_skele(skele_info: SkeleInfo, user_id: int, db: Session):
  skele = Skeletons(
    skelename = skele_info.skele_name,
    imgpath = skele_info.img_path,
    attributes = skele_info.attributes,
    creatorid = user_id
  )

  try:
    db.add(skele)
    db.flush()
    
    skele_relations = UserSkelesFav(
      userid = user_id,
      skeleid = skele.skeleid
    )
    db.add(skele_relations)
    
    skelechilds = skele_info.skele_childs
    if len(skelechilds) > 0:
      if not create_child_skeles(skele.skeleid, skelechilds, db):
        print("Failed to add child relations")
        return None
    db.commit()
    db.refresh(skele)
    return skele
  except SQLAlchemyError:
    db.rollback()
    return None
  
def edit_skele(skele_info: SkeleInfo, skele_id: int, db: Session):
  skele = db.query(Skeletons).filter(Skeletons.skeleid == skele_id).first()
  if not skele:
    return None
  
  skele.skelename = skele_info.skele_name
  skele.imgpath = skele_info.img_path
  skele.attributes = skele_info.attributes
  skelechilds = skele_info.skele_childs
  
  try:
    if len(skelechilds) > 0:
      if not create_child_skeles(skele.skeleid, skelechilds, db):
        print("Failed to add child relations")
        return None
    db.commit()
    db.refresh(skele)
    return {"id": skele.skeleid, "name": skele.skelename}
  except SQLAlchemyError:
    db.rollback()
    return None
  
def delete_skele(user_id: int, skele_id: int, db: Session):
  skele = db.query(Skeletons).filter(Skeletons.skeleid == skele_id).first()
  if not skele:
    return False
  if skele.creatorid != user_id:
    return False
  try:
    db.delete(skele)
    db.commit()
    return True
  except SQLAlchemyError:
    db.rollback()
    return False
  
def get_user_skeles(user_id: int, db: Session):
  rows = (
    db.query(Skeletons.skeleid, Skeletons.skelename, Skeletons.attributes)
    .join(UserSkelesFav, UserSkelesFav.skeleid == Skeletons.skeleid)
    .filter(UserSkelesFav.userid == user_id)
    .all()
  )
  return [{"id": r[0], "name": r[1], "attributes": r[2]} for r in rows]
  
def get_inv_skeles(inv_id: int, db: Session):
  rows = (
    db.query(Skeletons.skeleid, Skeletons.skelename, Skeletons.attributes)
    .join(InvSkeles, InvSkeles.skeleid == Skeletons.skeleid)
    .filter(InvSkeles.invid == inv_id)
    .all()
  )
  return [{"id": r[0], "name": r[1], "attributes": r[2]} for r in rows]

def favorite_skele(user_id: int, skele_id: int, db: Session):
  relation = UserSkelesFav(
    UserSkelesFav.userid == user_id,
    UserSkelesFav.skeleid == skele_id
  )
  try:
    db.add(relation)
    db.commit()
    db.refresh(relation)
    return True
  except SQLAlchemyError:
    db.rollback()
    return False
  

def unfavorite_skele(user_id: int, skele_id: int, db:Session):
  relation = db.query(UserSkelesFav).filter(UserSkelesFav.userid == user_id & UserSkelesFav.skeleid == skele_id).first()
  if not relation:
    return False
  try:
    db.delete(relation)
    db.commit()
    return True
  except SQLAlchemyError:
    db.rollback()
    return False

def create_child_skeles(parent_skele_id: int, child_skele_ids: list[int], db: Session):
  try:
    db.execute(
      delete(ChildSkeles).where(ChildSkeles.childskeleid.in_(child_skele_ids))
    )
  
    rows = [{"childskeleid": csi, "parentskeleid": parent_skele_id} for csi in child_skele_ids]
    
    db.execute(insert(ChildSkeles), rows)
    return True
  except SQLAlchemyError as e:
    db.rollback()
    print(e)
    return False
  
def get_child_skeles(skele_id: int, db: Session):
  return db.scalars(
    select(ChildSkeles.childskeleid).where(ChildSkeles.parentskeleid == skele_id)
  ).all()        
  
