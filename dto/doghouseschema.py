from pydantic import BaseModel
from typing import Optional
from datetime import time

class RegisterDoghouse(BaseModel):
    house_name : str
    owner_name : Optional[str]
    owner_email : Optional[str]
    owner_mobile : Optional[str]
    house_email: str
    house_mobile : str
    house_address : str
    house_license : str
    opening_time : time
    closing_time : time

