from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
class CreatePost(PostBase):
    pass

class UpdatePost(BaseModel):
    published: bool = True

class PostResponse(BaseModel):
    title : str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password : str
    

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    class Config:
        orm_mode = True