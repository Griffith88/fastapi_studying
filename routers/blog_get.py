from enum import Enum

from fastapi import APIRouter, Depends

router = APIRouter(prefix='/blog', tags=['blog'])


def required_functionality():
    return {'message': 'learning FastAPI is important'}


@router.get('/all',
            summary='Retrieve all blogs',
            description='This api call simulates fetching all blogs')
def get_all(page: int = 1, page_size: int = 20, req_param: dict = Depends(required_functionality)):
    return {f'message': f'Blog on {page} with page_size {page_size}', 'req': req_param}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{btype}')
def blog_type(btype: BlogType):
    return {'message': f'Blog type is {btype}'}


@router.get('/{pk}')
def params_get(pk: int):
    return {'message': f'Blog is {pk}'}
