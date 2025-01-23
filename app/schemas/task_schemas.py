from pydantic import BaseModel
from typing import Literal

class Task(BaseModel):
    name = str
    status = Literal['not_started', 'working', 'done']
    executor_id = int