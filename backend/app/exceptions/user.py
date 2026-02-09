class UserAlreadyExistsError(Exception):
    """Usuário já existe no sistema."""
    pass


class InvalidCredentialsError(Exception):
    """Credenciais inválidas."""
    pass
