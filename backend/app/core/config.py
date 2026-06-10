from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://aelp:aelp@db:5432/aelp"
    JWT_SECRET: str = "supersecret"
    ALGORITHM: str = "HS256"

settings = Settings()