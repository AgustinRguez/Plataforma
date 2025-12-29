from fastapi import APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends
from src.schema.schema_user import UserResponse, UserCreate
from src.crud.crud_user import register_user, get_user_by_id
from src.db.session import get_session

router_user = APIRouter()

@router_user.post("/users/add", response_model=UserResponse, status_code=201)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_session)):
    return await register_user(db=db, user_data=user_data)

@router_user.get("/users/get_by_id/{user_id_end}", response_model=UserResponse, status_code=200)
async def get_user_by_id_endpoint(user_id_end: int, db: AsyncSession = Depends(get_session)):
    user = await get_user_by_id(db=db, user_id=user_id_end)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error al obtener al cliente: {user_id_end}")
    return user

        