from sqlalchemy import Column, Integer, String
from .database import Base

class Fish(Base):
    __tablename__ = "fishes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    diet = Column(String, index=True)
