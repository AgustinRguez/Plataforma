from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from src.model.enum import UserEnum

class UserBase(BaseModel):
    name: str = Field(max_length=50)
    lastname: str = Field(max_length=50)
    email: str = Field(max_length=100)
    password: str = Field(min_length=8)
    role: UserEnum
    is_active: bool = True
    delete_at: Optional[datetime]

class UserResponse(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    role: UserEnum
    is_active: bool = True
    delete_at: Optional[datetime]
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str
    
class UserCreate(UserBase):
    pass