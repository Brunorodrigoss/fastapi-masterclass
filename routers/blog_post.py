from typing import Optional, List, Dict
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    number_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"hey1": "val1"}
    image: Optional[Image] = None

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

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(None,
        title='Title of the comment',
        description='Some description for comment_title',
        alias='commentTitle',
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
    v: List[str] = Query(['1.0','1.1', '1.2']),
    comment_id: int = Path(gt=5, le=10)

):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'comment_title': comment_title,
        'content': content,
        'version': v
    }