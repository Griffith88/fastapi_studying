from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from starlette import status

from db.models import DbUser
from hash import Hash
from schemas import UserBase


# CREATE USER
def create_user(db: Session, request: UserBase):
    new_user = DbUser(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# READ ALL USERS

def get_all_users(db: Session):
    return db.query(DbUser).all()


# READ SPECIAL USER

def get_user(db: Session, pk: int):
    user = db.query(DbUser).get(pk)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {pk} not exists!')
    return user


# UPDATE USER

def update_user(db: Session, pk: int, request: UserBase):
    user = db.query(DbUser).get(pk)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {pk} not exists!')
    user.email = request.email
    user.username = request.username
    user.password = Hash.bcrypt(request.password)
    db.commit()
    return 'ok'


# DELETE USER

def delete_user(db: Session, pk: int):
    user = db.query(DbUser).get(pk)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {pk} not exists!')
    db.delete(user)
    db.commit()
    return 'ok'
