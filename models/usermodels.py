from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from config.database import Base



class User(Base):
    __tablename__ = "users"  

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    mobile = Column(String)
    is_active = Column(Boolean, default=True)


    # petid = Column(Integer, ForeignKey("pet.id"))
    # pet = relationship("PetModel", back_populates="user")  


    reviews = relationship("ReviewModel", back_populates="user")
    services = relationship("ServiceModel", back_populates="user")
    stores = relationship("StoreModel", back_populates="user")
    # pet = relationship("PetModel", back_populates="user")

    # def __repr__(self):
    #     return f"<User {self.id}"

