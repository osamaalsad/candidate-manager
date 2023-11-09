from pydantic_settings import BaseSettings
from pydantic import MongoDsn


class MongoDBSettings(BaseSettings):
    MONGO_DSN: MongoDsn
    MONGODB_USERNAME: str
    MONGODB_PASSWORD: str


class SecretSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


class Settings(SecretSettings, MongoDBSettings):
    class Config:
        env_file = ".env"


settings = Settings()

