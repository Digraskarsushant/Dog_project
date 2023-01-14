from pydantic import BaseModel
from typing import Optional

# class PetUser(BaseModel):
#     userid: int
#     name : str
#     age : int
#     breed : str
#     gender : str 
#     height : int
#     weight : int 
#     color : str 
#     medical_history : str
    



class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
    mobile: str
    is_active: Optional[bool]
