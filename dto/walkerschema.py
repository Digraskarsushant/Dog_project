from pydantic import BaseModel
from typing import Optional


class RegisterWalker(BaseModel):
    name : str
    email : str
    mobile : str
    address : str
    driving_license  : str
    time_dur : int
    days : int