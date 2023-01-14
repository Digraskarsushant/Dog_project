from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from config.database import Base
from datetime import datetime
from models import usermodels


class ServiceModel(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    description = Column(String(255))
    
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="services")

    # def __repr__(self):
    #     return f"<servie {self.id}"



