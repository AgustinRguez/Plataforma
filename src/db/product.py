from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.db.base import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer)
    category = Column(String)

    #Relacion con el usuario
    user_id = Column(Integer, ForeignKey("users.id")) # de la tabla del usuario
    owner = relationship("User", back_populates="product")