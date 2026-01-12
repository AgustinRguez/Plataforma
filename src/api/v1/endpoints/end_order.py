from fastapi import APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends
from src.schema.schema_order import OrderCreate, OrderResponse
from src.schema.schema_product import ProductBase
from src.db.user import User
from src.crud.crud_order import create_order
from src.db.session import get_session
from src.api.v1.deps.deps import get_current_user

router_order = APIRouter()

@router_order.post("/orders/add_order", response_model=OrderResponse, status_code=201)
async def create_order_end(order_data: OrderCreate, db: AsyncSession = Depends(get_session), user_id: User = Depends(get_current_user)):
    try:
        result = await create_order(db=db, user_id=user_id.id, product_id=order_data.product_id, quantity=order_data.quantity)
        return result
    except Exception as e:
        if "no existe" in str(e):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        if "stock" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        if "No te podes comprar a vos mismo" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        if "No podes comprar productos que no estan activos" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error interno del servidor")
