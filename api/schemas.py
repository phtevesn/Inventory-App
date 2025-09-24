from pydantic import BaseModel

class SignUp(BaseModel):
    username: str
    firstname: str
    lastname: str
    email: str
    password: str