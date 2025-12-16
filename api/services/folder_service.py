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
  
  
def get_folder_and_pfolder(folder_id: int, db : Session):
  folder = db.query(Folders).filter(Folders.folderid == folder_id).first()
  
def delete_folder_inclusive(folder_id: int, db : Session):
  #deleting folder deletes all contents in folder, including other folders 
  folder = db.query(Folders).filter(Folders.folderid == folder_id).first()
  
def delete_folder_exclusive():
  #deleting folder deletes folder, moves everything into parent folder/removes folder 

def get_folders():
  

def edit_folder():
 #moving a folder 
 
