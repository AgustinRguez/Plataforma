from typing import Optional
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

# Es lo que se va a pasar a todos los endpoints protegidos
# si un usuario quiere crear algo o buscar algo enviara el jwt al servidor
class TokenData(BaseModel):
    user_id: Optional[str] = None