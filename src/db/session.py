from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from src.core import settings
from collections.abc import AsyncGenerator

engine = create_async_engine(settings.DATABASE_URL, echo=settings.ENVIRONMENT == "dev")
async_session = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit= False, class_=AsyncSession)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


