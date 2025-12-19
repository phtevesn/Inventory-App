from pydantic import BaseModel

class SignUp(BaseModel):
    username: str
    firstname: str
    lastname: str
    email: str
    password: str
    
class Login(BaseModel):
    usernameOrEmail: str
    password: str 
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: int
    #email: str | None = None

class CreateInv(BaseModel):
    invName: str
    
class SkeleInfo(BaseModel):
    skele_name: str
    img_path: str
    attributes: dict
    
class FolderInfo(BaseModel):
    folder_name: str
    inv_id: int
    parent_folder_id: int | None = None
    
class SkeleInstanceInfo(BaseModel):
    skele_id: int
    inv_id: int 
    folder_id: int
    count: int

class StatusInfo(BaseModel):
    status_name: str
    img_path: str
    does_it_count: bool