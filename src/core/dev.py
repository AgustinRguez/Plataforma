from .config import BaseConfig

class DevConfig(BaseConfig):
    ENVIRONMENT: str = "dev"
    DATABASE_URL: str = "postgresql+asyncpg://postgres:thisisshit@db:5432/plataforma_dev"
    MERCADO_PAGO_TOKEN: str = "token_dev"