from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.schema.schema_user import UserCreate
from src.db.user import User
from src.core.security import get_password_hash

async def register_user(db: AsyncSession, user_data: UserCreate):
    user_dict = user_data.model_dump()
    hash_pass = get_password_hash(password=user_data.password)
    user_dict["password"] = hash_pass
    db_user = User(**user_dict)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user_by_id(db: AsyncSession, user_id: int):
    user_to_obtain = select(User).where(User.id == user_id)
    result = await db.execute(user_to_obtain)
    return result.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str):
    user_to_obtain = select(User).where(User.email == email)
    result = await db.execute(user_to_obtain)
    return result.scalars().first()