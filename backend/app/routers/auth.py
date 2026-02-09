from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.exceptions.user import UserAlreadyExistsError, InvalidCredentialsError
from app.schemas.token import Token
from app.schemas.user import UserCredentials, UserRead
from app.services.user import authenticate_user, create_user


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post(
        "/signup",
        response_model=UserRead,
        status_code=status.HTTP_201_CREATED
)
def signup(
    user: UserCredentials,
    db: Session = Depends(get_db)
):
    """
    Chama a função que cria um novo usuário no sistema.
    Caso não exista um usuário com o email informado,
    um novo usuário é adicionado ao sistema e
    as informações deste são enviadas ao frontend.
    Caso um usuário com esse email já exista,
    lança uma exceção e retorna uma resposta HTTP ao frontend,
    informando que o email já está cadastrado.
    """
    try:
        return create_user(db, user.email, user.password)
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email já cadastrado"
        )


@router.post(
    "/login",
    response_model=Token,
    status_code=status.HTTP_200_OK
)
def login(
    user: UserCredentials,
    db: Session = Depends(get_db)
):
    """
    Chama a função que autentica o usuário.
    Caso as credenciais estejam corretas,
    autentica o usuário e retorna um token JWT.
    Caso estejam incorretas,
    lança uma exceção e retorna uma resposta HTTP ao frontend,
    Informando que o email ou a senha são inválidos.
    """
    try:

        return Token(
            access_token=authenticate_user(
                db,
                user.email,
                user.password
            )
        )

    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos",
            headers={"WWW-Authenticate": "Bearer"},
        )
