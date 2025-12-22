from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str = Field(max_length=50)
    lastname: str = Field(max_length=50)
    email: str = Field(max_length=100)
    password: str = Field(min_length=8)

class UserResponse(BaseModel):
    id: int
    name: str
    lastname: str
    email: str

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    pass