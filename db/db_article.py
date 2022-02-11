from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from db.models import DbArticle
from schemas import ArticleBase


# CREATE ARTICLE
def create_article(db: Session, request: ArticleBase):
    article = DbArticle(title=request.title,
                        content=request.content,
                        published=request.published,
                        user_id=request.creator_id)
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


# READ ALL ARTICLES
def read_all_article(db: Session):
    return db.query(DbArticle).all()


# READ SPECIAL ARTICLE
def read_special_article(db: Session, pk: int):
    article = db.query(DbArticle).get(pk)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Article with id {pk} not exists!')
    return article


# UPDATE ARTICLE
def update_article(db: Session, pk: int, request: ArticleBase):
    article = db.query(DbArticle).get(pk)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Article with id {pk} not exists!')
    article.title = request.title
    article.content = request.content
    article.published = request.published
    db.commit()
    return 'ok'


# DELETE ARTICLE
def delete_article(db: Session, pk: int):
    article = db.query(DbArticle).get(pk)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Article with id {pk} not exists!')
    db.delete(article)
    return 'ok'
