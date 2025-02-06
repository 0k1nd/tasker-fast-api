from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date ,datetime

class Users(SQLModel, table=True):
    userName: str = Field(default=None, unique=True, primary_key=True)
    name: str
    email: str = Field(unique=True)
    password: str
    created_at: date = Field(default=datetime.now())
    
    tasks: Optional[List["Task"]] = Relationship(back_populates="users")