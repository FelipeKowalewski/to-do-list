from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.core.exceptions import InternalDatabaseError
from app.core.security import create_access_token, get_password_hash, verify_password
from app.database.models import User
from app.exceptions.user import UserAlreadyExistsError, InvalidCredentialsError
from app.repositories.user import get_user_by_email, user_create


def create_user(db: Session, email: str, password: str) -> User:
    """
    Caso ainda não exista, cria novo usuário no sistema.
    """
    try:
        if get_user_by_email(db, email):
            raise UserAlreadyExistsError()
        user = User(
            email=email,
            hashed_password=get_password_hash(password)
        )
        return user_create(db, user)
    except SQLAlchemyError:
        db.rollback()
        raise InternalDatabaseError()


def authenticate_user(db: Session, email: str, password: str):
    """
    Caso credenciais estejam corretas, retorna token JWT do usuário.
    """
    try:
        user = get_user_by_email(db, email)
    except SQLAlchemyError:
        raise InternalDatabaseError()

    if not user:
        raise InvalidCredentialsError()

    if not verify_password(password, user.hashed_password):
        raise InvalidCredentialsError()

    token_data = {
        "sub": str(user.id)
    }

    access_token = create_access_token(token_data)

    return access_token
