from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from datetime import date ,datetime
from enum  import Enum

class Taskstatus(str, Enum):
    UPCOMING = "upcoming"
    PENDING = "pending"
    NOT_STARTED = "not_started"
    ACNIVE = "active"
    PRIORITY = "pririty"
    CANCELED = "canceled"
    

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    name: str = Field(default=None, index=True)
    status: Taskstatus
    created_at: date = Field(default=datetime.now())
    
    users: Optional[List["Users"]] = Relationship(back_populates="tasks")
    #test message for test commit