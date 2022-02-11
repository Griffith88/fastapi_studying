from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_article
from db.database import get_db
from schemas import ArticleDisplay, ArticleBase

router = APIRouter(prefix='/article', tags=['article', ])


# CREATE ARTICLE

@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db=db, request=request)


# GET ALL ARTICLES
@router.get('/all', response_model=List[ArticleDisplay])
def get_all_articles(db: Session = Depends(get_db)):
    return db_article.read_all_article(db)


# GET SPECIAL ARTICLE
@router.get('/{pk}', response_model=ArticleDisplay)
def get_special_article(pk: int, db: Session = Depends(get_db)):
    return db_article.read_special_article(db, pk)
