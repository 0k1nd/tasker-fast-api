from pydantic import BaseModel, EmailStr
from fastapi_users import schemas

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    
class UserRead(schemas.BaseUser[str]):
    pass