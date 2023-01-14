from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from config.database import Base


class VetModel(Base):
    __tablename__ = "vet"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    gender = Column(String(30))
    phone = Column(String(30))
    email = Column(String(30))
    degree = Column(String(30))
    address = Column(String(30))
    clinic_name = Column(String(30))
    registration_id = Column(String(30))
    opening_time = Column(String, default=10)
    closing_time = Column(String, default=5)

