from fastapi import APIRouter, status, Depends, Response, HTTPException
from app.schemas.users import CreateUser, UserOut
from .. import models, utils
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(tags=["users"], prefix="/users")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    
    # hash the password
    hash_password = utils.hash_password(user.password)
    user.password = hash_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user