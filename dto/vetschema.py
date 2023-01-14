from pydantic import BaseModel
from typing import Optional
from datetime import time

class VetSchema(BaseModel):

    name : str
    gender : str
    phone : str
    email : str
    degree : str
    address : str
    clinic_name : str 
    registration_id : str
    opening_time : time
    closing_time : time    
