from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models import Folders, Users
from schemas import FolderInfo

from db import get_db
from services.auth_service import get_current_user
from services.folder_service import (
  create_folder,
  edit_folder,
  delete_folder,
  get_child_folders,
  get_root_folders
)


router = APIRouter()

@router.post("/folder/create")
def createFolder(folder_info: FolderInfo, cur_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
  folder = create_folder(folder_info, cur_user.userid, db)
  if not folder:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Failed to create folder"
    )
  return folder

@router.put("/folder/edit")
def editFolder(folder_id: int, folder_name: str, db: Session = Depends(get_db)):
  new_folder_name = edit_folder(folder_id, folder_name, db)
  if not new_folder_name:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Failed to edit folder with folder id: {folder_id}"
    )
  return new_folder_name

@router.put("/folder/delete")
def deleteFolder(folder_id: int, db: Session = Depends(get_db)):
  if not delete_folder(folder_id, db):
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail=f"Failed to delete folder with folder id: {folder_id}"
    )
  return True

@router.put("/folder/root/get")
def getRootFolders(inv_id: int, db: Session = Depends(get_db)):
  folders = get_root_folders(inv_id, db)
  if not folders:
    raise HTTPException(
      status_code= status.HTTP_400_BAD_REQUEST,
      detail = f"Failed to get root folders for inventory with inventory id: {inv_id}"
    )
  return folders

@router.put("/folders/child/get")
def getChildFolders(folder_id: int, db: Session = Depends(get_db)):
  folders = get_child_folders(folder_id, db)
  if not folders:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail=f"Failed to get child folders from folder with folder id: {folder_id}"
    )
  return folders