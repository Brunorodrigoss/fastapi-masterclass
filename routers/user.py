from fastapi import APIRouter, Depends
from db.database import get_db
from db import db_user

from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.creater_user(db, request)

# Read user

# Update user

# Delete user

