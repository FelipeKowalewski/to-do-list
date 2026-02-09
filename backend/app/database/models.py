from sqlalchemy import Column, Integer, String, Enum, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.core.time import now
from app.database.database import Base
from app.database.type import TaskStatus

# Modelos Usuário e Tarefa
# Relacionamento:
# Um usuário pode ter múltiplas tarefas
# mas uma tarefa pode ter apenas um usuário


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending, nullable=False)
    created_date = Column(DateTime(timezone=True), default=now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="tasks")
