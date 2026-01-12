from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class OrderCreate(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)

class OrderResponse(OrderCreate):
    id: int
    unit_price: float
    total_price: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True