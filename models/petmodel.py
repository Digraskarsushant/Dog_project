from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from config.database import Base


class PetModel(Base):
    __tablename__ = "pet"

    id = Column(Integer, primary_key=True, index=True)
    caretaker_name = Column(String(50))
    name = Column(String(30))
    age = Column(Integer)
    breed = Column(String(30))
    gender = Column(String(10))
    height = Column(Integer)
    weight = Column(Integer)
    color = Column(String(30))
    medical_history = Column(String(30))
    
    
    # userid = Column(Integer, ForeignKey("users.id"), nullable=False)
    # user = relationship("User", back_populates="pet")


    # user = relationship("User", back_populates="pet") 
     


    

