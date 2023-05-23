from fastapi import FastAPI

import models
from database import engine
from routers import post, user

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}






    


























# from datetime import time
# from fastapi import FastAPI, status, HTTPException, Response, Depends
# from pydantic import BaseModel
# import psycopg2 
# from psycopg2.extras import RealDictCursor
# import models

# from sqlalchemy.orm import Session
# from database import engine, SessionLocal

# models.Base.metadata.create_all(bind=engine)


# app = FastAPI()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# class Post(BaseModel):
#     title : str
#     content : str
#     published : bool = True
    


# while True:
#     try: 
#         conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='youbitch', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Database connection failed")
#         print("Error", error)
#         time.sleep(2)



# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/sqlalchemy")
# def test_post(db: Session = Depends(get_db)):
#     return{"message": "success"}



# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     post = cursor.fetchall()
#     print(post)
#     return { 'data':post}

# @app.get("/posts/{id}")
# def get_post(id:str):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s """,(str(id)))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
#     return {"post_detail":post}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_post(post:Post):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return{"data": new_post}

# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s returning*""",(str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post==None:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
   
# @app.put("/posts/{id}")
# def update_post(id:int,post:Post):
#     cursor.execute("""UPDATE posts SET title = %s, content=%s, published=%s WHERE id = %s returning*""",(post.title,post.content,post.published,str(id),))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post==None:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#     return {"data": updated_post}
   