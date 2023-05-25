from datetime import time
from fastapi import status, HTTPException, Response, Depends, APIRouter
from sqlalchemy.orm import Session
import models, schemas, oauth2
from database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@router.get("/{id}",response_model=schemas.PostResponse)
def get_post(id : int,db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return post

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_post(post:schemas.CreatePost, db:Session= Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int, db: Session= Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

