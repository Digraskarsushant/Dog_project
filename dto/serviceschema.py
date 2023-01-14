from pydantic import BaseModel
from typing import Optional


class Service(BaseModel):
    
    name: str
    description: str
    # owner_id: int
