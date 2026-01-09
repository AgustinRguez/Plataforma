from fastapi import APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends
from src.db.user import User
from src.schema.schema_user import UserResponse, UserCreate, UserLogin
from src.schema.token import Token
from src.crud.crud_user import register_user, get_user_by_id, get_user_by_email, update_state_user
from src.db.session import get_session
from src.core.security import verify_password
from src.core.jwt import create_access_token
from src.api.v1.deps.deps import get_current_user


router_user = APIRouter()

@router_user.post("/users/add", response_model=UserResponse, status_code=201)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_session)):
    user_check = await get_user_by_email(db=db, email=user_data.email)
    if user_check:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya existe")
    user = await register_user(db=db, user_data=user_data)
    return user

@router_user.get("/users/get_by_id/{user_id_end}", response_model=UserResponse, status_code=200)
async def get_user_by_id_endpoint(user_id_end: int, db: AsyncSession = Depends(get_session)):
    user = await get_user_by_id(db=db, user_id=user_id_end)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error al obtener al cliente: {user_id_end}")
    return user

@router_user.post("/users/login", response_model=Token, status_code=200)
async def get_user_by_id_endpoint(data: UserLogin, db: AsyncSession = Depends(get_session)):
    user = await get_user_by_email(db=db, email=data.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error en la contraseña o email")
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El usuario esta desactivado para el login")
    if not verify_password(password_verify=data.password, hashed_password=user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error en la contraseña o email")
    access_token = create_access_token(data={"sub": str(user.id), "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

@router_user.get("/users/read", response_model=UserResponse, status_code=200)
async def read_user(current_user = Depends(get_current_user)):
    return current_user

@router_user.patch("/users/update_state", response_model=UserResponse, status_code=200)
async def change_state(db: AsyncSession = Depends(get_session), user_id: User = Depends(get_current_user)):
    update_user = await update_state_user(db=db, user_id=user_id.id)
    return update_user