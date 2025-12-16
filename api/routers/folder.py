from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models import Folders
from schemas import FolderInfo

from db import get_db
from services.folder_service import (
    create_folder,
    edit_folder,
    delete_folder,
    get_child_folders,
    get_root_folders
)

router = APIRouter()

@router.post("/folder/create")
def createFolder(folder_info: FolderInfo, user_id: )