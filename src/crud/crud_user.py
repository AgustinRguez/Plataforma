from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.schema.schema_user import UserCreate
from src.db.user import User

async def register_user(db: AsyncSession, user_data: UserCreate):
    add_user = User(**user_data.model_dump())
    db.add(add_user)
    await db.commit()
    await db.refresh(add_user)
    return add_user