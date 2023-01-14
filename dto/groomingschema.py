from pydantic import BaseModel
from typing import Optional
from datetime import time

class groomingschema(BaseModel):
    
    name : str
    provider_name : str
    storename : str
    phone : str
    address : str
    regestration_no : str
    opentime : time
    closetime : time
