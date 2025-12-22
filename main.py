from fastapi import FastAPI
from src.api.v1.endpoints.end_product import router as product
from src.api.v1.endpoints.end_user import router_user as user
from src.db.product import Product
from src.db.user import User

app = FastAPI(title="Plataforma de venta")
app.include_router(product, prefix="/v1", tags=["products"])
app.include_router(user, prefix="/v1", tags=["users"])

@app.get("/health")
async def get_health():
    return {"status": "ok"} 
