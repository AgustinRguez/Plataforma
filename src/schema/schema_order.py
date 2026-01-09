from typing import Optional
from pydantic import BaseModel, Field

class OrderCreate(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)