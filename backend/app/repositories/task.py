from sqlalchemy.orm import Session

from app.database.models import Task


def task_create(db: Session, task: Task) -> Task:
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks_by_user(db: Session, user_id: int) -> list[Task]:
    return db.query(Task).filter(Task.user_id == user_id).all()


def get_task_by_id(db: Session, task_id: int, user_id: int) -> Task | None:
    return (
        db.query(Task)
        .filter(Task.id == task_id, Task.user_id == user_id)
        .first()
    )


def task_delete(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()
