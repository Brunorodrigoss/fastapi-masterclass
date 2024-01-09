from typing import Optional
from fastapi import APIRouter
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

@router.post('/new')
def create_blog(blog: BlogModel):
    return { 'data': blog}