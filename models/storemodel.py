import sqlalchemy as sa
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Boolean, DateTime
from sqlalchemy.sql.schema import ForeignKey
from config.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class StoreModel(Base):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    city = Column(String(30))
    country = Column(String(30))
    currency = Column(String(3))
    domain = Column(String(30),nullable = False)
    phone = Column(String(30),nullable = False)
    street = Column(String(30))
    zipcode = Column(String(30))
    email = Column(String(256), unique=True,nullable = False)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="stores")

# class StoreCreate(Base):
#     __tablename__ = "shop"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(30))
#     city = Column(String(30))
#     country = Column(String(30))
#     currency = Column(String(3))
#     zipcode = Column(String(30))
#     street = Column(String(30))
    



