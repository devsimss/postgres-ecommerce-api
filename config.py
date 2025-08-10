
import os

# Basit bir ayar modülü. Üretimde pydantic-settings gibi bir çözüm daha iyi olur.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/shop")
APP_ENV = os.getenv("APP_ENV", "dev")
