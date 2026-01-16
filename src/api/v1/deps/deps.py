from src.model.enum import UserEnum
from src.db.user import User
from src.core.jwt import decode_token
from src.db.session import get_session
from src.crud.crud_user import get_user_by_id
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer  

oauth_scheme = OAuth2PasswordBearer(tokenUrl="v1/auth/login")

async def get_current_user(token: str = Depends(oauth_scheme), db = Depends(get_session)):
    payload = decode_token(token=token)
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token erroneo")
    user_obtain = await get_user_by_id(db=db, user_id=int(user_id))
    if user_obtain is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not user_obtain.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El usuario no esta activo")
    return user_obtain

async def get_current_admin(user: User = Depends(get_current_user)):
    current_user = user
    if not current_user.role == UserEnum.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Solo los admin puede reactivar usuarios")
    return current_user
