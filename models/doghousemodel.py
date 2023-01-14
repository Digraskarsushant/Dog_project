from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.database import Base



class DoghouseModel(Base):
    __tablename__ = "doghouse"  

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    house_name = Column(String(200))
    owner_name = Column(String(200))
    house_email = Column(String(200))
    owner_email = Column(String(200))
    house_mobile = Column(String(13))
    owner_mobile = Column(String(13))
    house_address = Column(String(200))
    house_license = Column(String(20))
    opening_time = Column(String, default = 10)
    closing_time = Column(String, default = 5)