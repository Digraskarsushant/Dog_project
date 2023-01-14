from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from config.database import Base



class GroomingModel(Base):
    __tablename__="grooming"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    provider_name = Column(String(30))
    storename = Column(String(30))
    phone = Column(String(30))
    address = Column(String(30))
    regestration_no = Column(String(30))    
    opentime = Column(String, default=10)
    closetime = Column(String, default=5)


    