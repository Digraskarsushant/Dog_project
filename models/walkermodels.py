from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.database import Base



class WalkerModel(Base):
    __tablename__ = "walker"  

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    name = Column(String(200))
    email = Column(String(200))
    mobile = Column(String(13))
    address = Column(String(200))
    driving_license = Column(String(20))
    time_dur = Column(Integer, default=1)
    days = Column(Integer, default=1)