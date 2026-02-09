from datetime import datetime
from pytz import timezone


TIMEZONE = timezone("America/Sao_Paulo")


def now():
    """
    Retorna a data e hora atual, da timezone especifica do usuário.
    """
    return datetime.now(TIMEZONE)
