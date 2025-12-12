from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(max_length=100)
    description: str
    price: float = Field(gt=0.0)
    stock: int = Field(ge=0)
    category: str

class ProductResponse(BaseModel):
    id: int
    user_id: int

    class Config:
        #Permite que pydantic lea datos directamente desde un modelo ORM
        from_atributtes = True
        
class ProducCreate(ProductBase):
    pass