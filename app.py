from db.database import engine
from routers import blog_get, blog_post,user
from fastapi import FastAPI
from db import models

firstApp = FastAPI()
firstApp.include_router(blog_get.router)
firstApp.include_router(blog_post.router)
firstApp.include_router(user.router)


@firstApp.get('/')
def home():
    return {'message': 'Hello World!'}


models.Base.metadata.create_all(engine)
