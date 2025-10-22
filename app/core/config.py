from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    APP_NAME: str = "CollabHub"
    FRONTEND_ORIGIN: str = "http://localhost:5173"

    class Config:
        env_file = ".env"

settings = Settings()
