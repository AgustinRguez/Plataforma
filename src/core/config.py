from pydantic_settings import BaseSettings

class BaseConfig(BaseSettings): 
    #Defino las variables que la app necesita, el .env guarda los valores concretos, no elige entorno
    PROJECT_NAME: str = "Plataforma de venta"
    JAEGER_HOST: str = "jaeger"
    JAEGER_PORT: int = 6831

    class Config:
        env_file = ".env"
