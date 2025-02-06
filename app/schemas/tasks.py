from pydantic import BaseModel
from app.models import Taskstatus
from datetime import datetime

class TaskCreate(BaseModel):
    name: str
    status: Taskstatus 
    users_id: int 
    
class TaskResponsw(BaseModel):
    id: int
    name: str
    status: str
    created_at: datetime
    
    users: int