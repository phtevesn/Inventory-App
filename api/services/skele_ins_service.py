from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import SkeleInstances
from schemas import SkeleInstanceInfo


def create_skele_instance(instance_info: SkeleInstanceInfo, user_id: int , db: Session):
  skele_instance = SkeleInstances(
    skeleid = instance_info.skele_id,
    invid = instance_info.inv_id,
    folderid = instance_info.folder_id,
    count = instance_info.count
  )

  try:
    db.add(skele_instance)
    db.commit()
    db.refresh(skele_instance)
    return skele_instance
  except SQLAlchemyError:
    db.rollback()
    return None
  
def edit_skele_instance(instance_id: int, folder_id: int, count: int, db: Session):
  skele_instance = db.query(SkeleInstances).filter(SkeleInstances.skeleinstanceid == instance_id).first()
  if not skele_instance:
    return None
  
  skele_instance.folderid = folder_id 
  skele_instance.count = count

  try:
    db.commit()
    db.refresh(skele_instance)
    return skele_instance
  except SQLAlchemyError:
    db.rollback()
    return None

def delete_skele_instance(instance_id: int, db: Session):
  skele_instance = db.query(SkeleInstances).filter(SkeleInstances.skeleinstanceid == instance_id).first()
  if not skele_instance:
    return None
  
  try:
    db.delete(skele_instance)
    db.commit()
    return True
  except SQLAlchemyError:
    db.rollback()
    return None
  
def get_skele_instances(inv_id: int, db:Session):
  skele_instances = db.query(SkeleInstances).filter(SkeleInstances.invid == inv_id).all()
  return skele_instances 
  