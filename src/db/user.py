from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Float, Enum, Boolean, DateTime
from src.db.base import Base
from src.model.enum import UserEnum

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    lastname = Column(String, unique=False, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    role = Column(Enum(UserEnum, name="user_role_enum"), nullable=False)
    is_active = Column(Boolean, default=True)
    delete_at = Column(DateTime, nullable=True)

    product = relationship("Product", back_populates="owner")
    orders = relationship("Order", back_populates="user")