from functools import lru_cache
from pydantic import (
    BaseSettings, 
    Field
)

class Settings(BaseSettings):
    secret_key: str = Field(..., env='SECRET_KEY')
    jwt_algorithm: str = Field(default='HS256')
    session_duration: int = Field(default=86400)
    mongo_uri: str = Field(..., env='MONGO_URI')

    class Config:
        env_file = '.env'

@lru_cache
def get_settings():
    return Settings()