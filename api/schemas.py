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