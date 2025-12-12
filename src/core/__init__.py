import os
from .config import BaseConfig

env = os.getenv("ENVIRONMENT", "main") #lectura al sistema

if env == "main":
    from .prd import PrdConfig as Settings
else:
    from .dev import DevConfig as Settings

settings = Settings()