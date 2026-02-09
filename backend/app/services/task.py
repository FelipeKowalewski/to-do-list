from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.exceptions import InternalDatabaseError
from app.database.models import Task
from app.exceptions.task import TaskNotFoundError
from app.repositories.task import (
    task_create,
    get_tasks_by_user,
    get_task_by_id,
    task_delete,
)


def create_user_task(
    db: Session,
    user_id: int,
    task_data: dict
) -> Task:
    """
    Cria uma task para o usuário.
    """
    try:
        task = Task(
            **task_data,
            user_id=user_id
        )
        return task_create(db, task)
    except SQLAlchemyError:
        db.rollback()
        raise InternalDatabaseError()


def list_user_tasks(
    db: Session,
    user_id: int
) -> list[Task]:
    try:
        return get_tasks_by_user(db, user_id)
    except SQLAlchemyError:
        raise InternalDatabaseError()


def update_user_task(
    db: Session,
    task_id: int,
    user_id: int,
    task_data: dict
) -> Task:
    try:
        task = get_task_by_id(db, task_id, user_id)

        if not task:
            raise TaskNotFoundError()

        for field, value in task_data.items():
            setattr(task, field, value)

        db.commit()
        db.refresh(task)
        return task
    except SQLAlchemyError:
        db.rollback()
        raise InternalDatabaseError()


def delete_user_task(
    db: Session,
    task_id: int,
    user_id: int
) -> None:
    try:
        task = get_task_by_id(db, task_id, user_id)

        if not task:
            raise TaskNotFoundError()

        task_delete(db, task)
    except SQLAlchemyError:
        db.rollback()
        raise InternalDatabaseError()
