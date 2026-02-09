from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.models import User
from app.dependencies.db import get_db
from app.dependencies.auth import get_current_user
from app.exceptions.task import TaskNotFoundError
from app.schemas.task import TaskCreate, TaskUpdate, TaskRead
from app.services.task import (
    create_user_task,
    list_user_tasks,
    update_user_task,
    delete_user_task,
)


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Chama a função que cria uma nova tarefa.
    """
    return create_user_task(db, current_user.id, task.model_dump())


@router.put(
    "/{task_id}",
    response_model=TaskRead
)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Chama função que atualiza os campos enviados pelo frontend
    de um objeto de tarefa selecionado. Caso a tarefa não for
    encontrada no banco de dados, lança uma exceção informando
    que a tarefa não foi encontrada.
    """
    try:
        return update_user_task(
            db,
            task_id,
            current_user.id,
            task.model_dump(exclude_unset=True)
        )
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )


@router.get(
    "",
    response_model=list[TaskRead]
)
def list_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Chama a função que retorna uma lista de todas as tarefas
    do usuário atualmente logado no sistema.
    """
    return list_user_tasks(db, current_user.id)


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Chama a função que deleta a tarefa enviada pelo frontend.
    Caso a tarefa não for encontrada no banco de dados, lança
    uma exceção informando que a tarefa não foi encontrada.
    """
    try:
        delete_user_task(db, task_id, current_user.id)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
