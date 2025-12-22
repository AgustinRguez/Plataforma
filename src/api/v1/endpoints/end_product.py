from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends
from src.schema.schema_product import ProductResponse, ProductCreate
from src.crud.crud_product import register_product, get_products, get_product_by_id
from src.db.session import get_session

router = APIRouter()

@router.post("/products/add", response_model=ProductResponse, status_code=201)
async def create_product(product_data: ProductCreate, db: AsyncSession = Depends(get_session)):
    return await register_product(db=db, product_data=product_data)
    
@router.get("/products/get_all", response_model=list[ProductResponse], status_code=201)
async def get_all_products(db: AsyncSession = Depends(get_session)):
    return await get_products(db)

@router.get("/products/{product_id}", response_model=list[ProductResponse], status_code=201)
async def get_product_by_id(product_id: int, db: AsyncSession = Depends(get_session)):
    return await get_product_by_id(product_id=product_id, db=db)