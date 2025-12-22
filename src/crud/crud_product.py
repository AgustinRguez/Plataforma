from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.schema.schema_product import ProductCreate
from src.db.product import Product

async def register_product(db: AsyncSession, product_data: ProductCreate):
    add_product = Product(**product_data.model_dump())
     # dictionary unpacking, le pasa cada par clave-valor al modelo de SQLAlchemy 
    db.add(add_product)
    await db.commit()
    await db.refresh(add_product)
    return add_product

async def get_products(db: AsyncSession):
    query = select(Product)
    result = await db.execute(query)
    return result.scalars().all() #devuelve el primer elemento de cada fila

async def get_product_by_id(db: AsyncSession, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await db.execute(query)
    return result.scalars().first()