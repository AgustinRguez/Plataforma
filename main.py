from fastapi import FastAPI
from src.api.v1.endpoints.product import router as product

app = FastAPI(title="Plataforma de venta")
app.include_router(product, prefix="/v1", tags=["products"])

@app.get("/health")
async def get_health():
    return {"status": "ok"} 
