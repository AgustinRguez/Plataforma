from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

SECRET_KEY = "isnotaclave"
ALGORITHM = "HS256"

def create_access_token(data: dict, expire_delta: timedelta = None):
    to_encode = data.copy() # se toma datos del usuario y se hace una copia
    expire = datetime.now(timezone.utc) + (expire_delta or timedelta(minutes=10))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode,  SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise Exception(f"Token expirado: {e}")

