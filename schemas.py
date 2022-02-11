from typing import Optional, List, Dict

from pydantic import BaseModel


# inside UserDisplay
class ArticleDisplayWithUser(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[ArticleDisplayWithUser] = []

    class Config:
        orm_mode = True


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, int] = {'key1': 123}


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class UserWithArticleDisplay(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: str
    user: UserWithArticleDisplay

    class Config:
        orm_mode = True
