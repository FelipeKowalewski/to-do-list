from datetime import timedelta

from fastapi import HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings
from app.core.time import now


# definição de utilização do hash bcrypt
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_password_hash(password: str) -> str:
    """
    Retorna hash da senha recebida.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Retorna True se a senha recebida for compativel com o hash recebido.
    Retorna False caso contrário.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Retorna o token JWT do usuário com base nas informações,
    id de usuário e tempo de expiração do token.
    """
    to_encode = data.copy()

    expire = now() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt


# decodifica token de segurança
def decode_access_token(token: str) -> dict:
    """
    Retorna informações do respectivo usuário com base no token recebido.
    Caso ocorra um JWTError, lança exceção de token inválido ou expirado.
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
