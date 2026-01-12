from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends
from src.db.user import User
from src.schema.schema_product import ProductResponse, ProductCreate, ProductList, ProductUpdate
from src.crud.crud_product import register_product, get_products, update_product, get_product_by_user, get_product_by_id
from src.db.session import get_session
from src.api.v1.deps.deps import get_current_user

router = APIRouter()

@router.post("/products/add", response_model=ProductResponse, status_code=201)
async def create_product(product_data: ProductCreate, db: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    return await register_product(db=db, product_data=product_data, user=user.id)
    
@router.get("/products/get_all", response_model=list[ProductList], status_code=200)
async def get_all_products(db: AsyncSession = Depends(get_session)):
    return await get_products(db)

@router.get("/products/get_id/{product_id}", response_model=ProductList, status_code=200)
async def get_all_products(product_id: int, db: AsyncSession = Depends(get_session)):
    return await get_product_by_id(db=db, product_id=product_id)

@router.patch("/products/update/{product_id}", response_model=ProductUpdate, status_code=200)
async def patch_product(product_id: int, product_data: ProductUpdate, user_id: User = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    update_data = await update_product(db=db, product_id=product_id, product_data=product_data, user_id=user_id.id)
    return update_data

@router.get("/products/by_user", response_model=list[ProductList], status_code=200)
async def get_all_by_user(db: AsyncSession = Depends(get_session), user_id: User = Depends(get_current_user)):
    return await get_product_by_user(db=db, user_id=user_id.id)