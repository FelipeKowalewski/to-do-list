from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.exceptions import AuthenticationError
from app.core.security import decode_access_token
from app.database.models import User
from app.dependencies.db import get_db
from app.repositories.user import get_user_by_id


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    """Dependência retorna o usuário que está logado no sistema."""
    payload = decode_access_token(token)

    try:
        sub = payload.get("sub")
        if sub is None:
            raise AuthenticationError()

        user_id = int(sub)

        user = get_user_by_id(db, user_id)
        if not user:
            raise AuthenticationError()
    except (ValueError, AuthenticationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user
