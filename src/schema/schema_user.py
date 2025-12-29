from pydantic import BaseModel, Field
from src.model.enum import UserEnum

class UserBase(BaseModel):
    name: str = Field(max_length=50)
    lastname: str = Field(max_length=50)
    email: str = Field(max_length=100)
    password: str = Field(min_length=8)
    role: UserEnum

class UserResponse(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    role: UserEnum
    
    class Config:
        from_attributes = True

class UserCreate(UserBase):
    pass