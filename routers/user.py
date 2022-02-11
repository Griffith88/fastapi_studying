from typing import List

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm.session import Session

from db import db_user
from db.database import get_db
from schemas import UserBase, UserDisplay

router = APIRouter(prefix='/user', tags=['user', ])


# CREATE USER

@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# READ ALL USERS

@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# READ SPECIAL USER

@router.get('/{pk}', response_model=UserDisplay)
def get_special_user(pk, db: Session = Depends(get_db)):
    return db_user.get_user(db, pk)


# UPDATE USER

@router.post('/{pk}/update')
def update_user(pk: int, db: Session = Depends(get_db),
                request: UserBase = Body(description='information to update', default=...)):
    return db_user.update_user(db, pk, request)


# DELETE USER

@router.delete('/{pk}/delete')
def delete(pk: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, pk)
