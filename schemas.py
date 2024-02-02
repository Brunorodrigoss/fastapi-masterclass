from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

# Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class Config():
        orm_mode = True

class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    class Config():
        orm_mode = True

# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode = True
        
class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config():
        orm_mode = True

class ProductBase(BaseModel):
    title: str
    description: str
    price: float