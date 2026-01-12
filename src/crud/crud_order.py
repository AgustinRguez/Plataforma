from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.product import Product
from src.db.order import Order
from src.model.enum import TypeEnum, StatusEnum
from datetime import datetime

async def create_order(db: AsyncSession, user_id: int, product_id: int, quantity: int): #la resta de stock es a la bdd no al pydantic
    producto_obtener = await db.execute(select(Product).where(Product.id == product_id))
    db_product = producto_obtener.scalar_one_or_none()
    if not db_product:
        raise Exception("El producto no existe")
    if db_product.user_id == user_id:
        raise Exception(f"No te podes comprar a vos mismo")
    if not db_product.is_active:
        raise Exception(f"No podes comprar productos que no estan activos")
    if db_product.stock < quantity:
        raise Exception(f"Cantidad por encima del stock permitido")

    db_product.stock -= quantity        
    total = db_product.price * quantity
    add_order = Order(buyer_id=user_id,
                       product_id=db_product.id,
                        quantity=quantity,
                        unit_price=db_product.price,
                        total_price=total,
                        type=TypeEnum.B,
                        status=StatusEnum.in_process)
    db.add(add_order)
    try:
        await db.commit()
        await db.refresh(add_order)
        return add_order
    except Exception as e:
        await db.rollback()
        raise e
        