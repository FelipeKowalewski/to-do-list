from sqlalchemy.orm import Session

from app.database.models import User


def get_user_by_id(db: Session, id: int) -> User | None:
    return (
        db.query(User)
        .get(id)
    )


def get_user_by_email(db: Session, email: str) -> User | None:
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def user_create(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
