from sqlalchemy.ext.asyncio import AsyncSession
from src.schema.product import ProductCreate
from src.db.product import Product

async def register_product(db: AsyncSession, product_data: ProductCreate, user_id: int):
    add_product = Product(**product_data.model_dump(), user_id=user_id)
     # dictionary unpacking, le pasa cada par clave-valor al modelo de SQLAlchemy 
    db.add(add_product)
    await db.commit()
    await db.refresh(add_product)
    return add_product