from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends
from src.schema.schema_product import ProductResponse, ProductCreate, ProductList, ProductUpdate
from src.crud.crud_product import register_product, get_products, update_product
from src.db.session import get_session

router = APIRouter()

@router.post("/products/add", response_model=ProductResponse, status_code=201)
async def create_product(product_data: ProductCreate, db: AsyncSession = Depends(get_session)):
    return await register_product(db=db, product_data=product_data)
    
@router.get("/products/get_all", response_model=list[ProductList], status_code=200)
async def get_all_products(db: AsyncSession = Depends(get_session)):
    return await get_products(db)

@router.patch("/products/update/{product_id}", response_model=ProductUpdate, status_code=200)
async def patch_product(product_id: int, product_data: ProductUpdate, db: AsyncSession = Depends(get_session)):
    update_data = await update_product(db=db, product_id=product_id, product_data=product_data)
    return update_data