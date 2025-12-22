from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Float
from src.db.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    lastname = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    
    product = relationship("Product", back_populates="owner")