from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends
from src.schema.schema_user import UserResponse, UserCreate
from src.crud.crud_user import register_user
from src.db.session import get_session

router_user = APIRouter()

@router_user.post("/users/add", response_model=UserResponse, status_code=201)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_session)):
    return await register_user(db=db, user_data=user_data)