import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer  
from jwt import decode_token

oauth_scheme = OAuth2PasswordBearer(tokenUrl="v1/auth/login")

def get_password_hash(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password=password.encode('utf-8'), salt=salt)
    return hashed.decode('utf-8')

def verify_password(password_verify: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password=password_verify.encode('utf-8'), hashed_password=hashed_password.encode('utf-8'))

def get_current_user(token: str = Depends(oauth_scheme)):
    payload = decode_token(token=token) #es parte de oauth, tiene que obtener el decode de la firma del token jwt para validar que es correcto
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token erroneo")
    #se retorna el objeto usuario, pasar funcion a api