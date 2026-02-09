from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Classe de definição de configurações do banco de dados
    e do token de segurança do usuário.
    """
    # Banco de dados
    DATABASE_URL: str = "sqlite:///./app.db"

    # Segurança
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 7200

    class Config:
        env_file = ".env"


settings = Settings()
