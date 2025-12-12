from fastapi import FastAPI
from src.db.session import engine
from db.base import Base

app = FastAPI(title="Plataforma de venta")

@app.get("/health")
async def get_health():
    return {"status": "ok"}
