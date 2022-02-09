from typing import Optional, List, Dict

from fastapi import APIRouter, Path, Body, Query
from pydantic import BaseModel

from schemas import BlogModel

router = APIRouter(prefix='/blog', tags=['blog', ])





@router.post('/new/{pk}')
def create_blog(blog: BlogModel, pk: int, version: int = 1):
    return {'id': pk,
            'data': blog,
            'version': version}


@router.post('/new/{pk}/comment', tags=['comment'])
def create_comment(blog: BlogModel,
                   pk: int = Path(None, gt=3, ),
                   comment_id: int = Query(1,
                                           alias='commentId',
                                           title='Id of comment',
                                           description='Some description of comment_id'),
                   content: str = Body(..., min_length=10, regex=r'^[a-z\s]*$'),
                   version: Optional[List[str]] = Query(None)
                   ):
    return {'data': blog,
            'id': pk,
            'comment_id': comment_id,
            'content': content,
            'version': version,
            }



