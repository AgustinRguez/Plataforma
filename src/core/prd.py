from .config import BaseConfig

class PrdConfig(BaseConfig):
    ENVIRONMENT: str = "main"
    DATABASE_URL: str = "postgresql+asyncpg://postgres:36025147@db:5432/plataforma_prd"
    MERCADO_PAGO_TOKEN: str = "token_prd"