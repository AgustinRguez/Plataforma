from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, Float, ForeignKey, Enum, DateTime
from src.db.base import Base
from src.model.enum import TypeEnum, StatusEnum
from datetime import datetime

class Order(Base):
    __tablename__= "orders"
    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    type = Column(Enum(TypeEnum), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")