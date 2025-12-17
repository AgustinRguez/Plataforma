from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends
from src.schema.product import ProductResponse, ProductCreate
from src.crud.crud_product import register_product
from src.db.session import get_session

router = APIRouter()

@router.post("/products/add", response_model=ProductResponse, status_code=201)
async def create_product(product_data: ProductCreate, db: AsyncSession = Depends(get_session)):
    user_id = 1
    return await register_product(db, product_data, user_id=user_id)
    