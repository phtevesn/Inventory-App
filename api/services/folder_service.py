from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Folders
from schemas import FolderInfo

def create_folder(folder_info: FolderInfo, user_id: int, db: Session):
  folder = Folders(
     foldername = folder_info.folder_name,
     invid = folder_info.inv_id,
     parentfolderid = folder_info.parent_folder_id
  )
  
  try:
    db.add(folder)
    db.commit()
    db.refresh(folder)
    return True
  except SQLAlchemyError:
    db.rollback()
    return False


def edit_folder(folder_id: int, folder_name: str, db: Session):
  folder = db.query(Folders).filter(Folders.folderid == folder_id).first()
  if not folder:
    return None
  
  folder.foldername = folder_name

  try:
    db.commit()
    db.refresh(folder)
    return folder.foldername
  except SQLAlchemyError:
    db.rollback()
    return None
 
  
def delete_folder(folder_id: int, db : Session):
  #deleting folder deletes all contents in folder, including other folders and skele_instances
  folder = db.query(Folders).filter(Folders.folderid == folder_id).first()
  if not folder:
    return None
  
  try:
    db.delete(folder)
    db.commit()
    return True
  except SQLAlchemyError:
    db.rollback()
    return False

  
def get_root_folders(inv_id: int, db: Session):
  folders = db.query(Folders).filter(Folders.invid == inv_id, Folders.parentfolderid == None).all()
  return folders
  
def get_child_folders(folder_id: int, db: Session):
  folders = db.query(Folders).filter(Folders.folderid == folder_id).all()
  return folders
