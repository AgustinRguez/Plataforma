from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends
from src.schema.schema_order import OrderCreate
from src.schema.schema_product import ProductBase
from src.db.user import User
from src.crud.crud_product import register_product, get_products, update_product, get_product_by_user
from src.db.session import get_session
from src.api.v1.deps.deps import get_current_user

router_order = APIRouter()

@router_order.post("/orders", response_model=OrderCreate, status_code=201)
async def create_order(product: ProductBase, db: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    pass
