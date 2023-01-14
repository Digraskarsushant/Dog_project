from pydantic import BaseModel
from typing import Optional

# class UserPet(BaseModel):
#     user_id: int
#     name : str
#     age : int
#     breed : str
#     gender : str 
#     height : int
#     weight : int 
#     color : str 
#     medical_history : str
    





class PetSchema(BaseModel):
    # userid: int
    caretaker_name: str
    name : str
    age : int
    breed : str
    gender : str 
    height : int
    weight : int 
    color : str 
    medical_history : str