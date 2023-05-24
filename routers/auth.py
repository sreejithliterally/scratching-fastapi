from datetime import time
from fastapi import status, HTTPException, Response, Depends, APIRouter
from sqlalchemy.orm import Session
import models, schemas, utils
from database import get_db



router = APIRouter(
    tags=['Auth']
)

@router.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email== user_credentials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')
    
    return {
        "token": "ex token"
    }