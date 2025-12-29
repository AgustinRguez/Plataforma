from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.schema.schema_product import ProductCreate, ProductUpdate
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

async def update_product(db: AsyncSession, product_id: int, product_data: ProductUpdate):
    query = select(Product).where(Product.id == product_id)
    result = await db.execute(query)
    db_product = result.scalars().first()
    if not db_product:
        return None
    update_data = product_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)
    await db.commit()
    await db.refresh(db_product)
    return db_product
