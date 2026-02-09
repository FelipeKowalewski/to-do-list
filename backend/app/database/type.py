import enum


class TaskStatus(enum.Enum):
    """
    Definição das opções de status.
    """
    pending = "pending"
    in_progress = "in_progress"
    done = "done"
