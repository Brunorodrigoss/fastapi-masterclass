from typing import Optional, List
from fastapi import APIRouter, Query, Body
from pydantic import BaseModel

class BlogModel(BaseModel):
    title: str
    content: str
    number_comments: int
    published: Optional[bool]

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return { 
        'id': id,
        'data': blog,
        'version': version    
    }

@router.post('/new/{id}/comment')
def create_comment(
    blog: BlogModel,
    id: int,
    comment_id: int = Query(
        None,
        title='Id of the comment',
        description='Some description for comment_id',
        alias='commentId',
        deprecated=True
    ),
    #content: str = Body('ho how are you')
    # content: str = Body(...)
    # content: str = Body(Ellipsis)

    content: str = Body(..., 
        min_length=10,
        max_length=12,
        regex='^[a-z\s]*$'
    ),
    # v: List[str] = Query(None)
    v: List[str] = Query(['1.0','1.1', '1.2'])

):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content,
        'version': v
    }