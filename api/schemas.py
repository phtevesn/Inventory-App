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
    