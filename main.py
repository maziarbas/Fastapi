from typing import ContextManager, Optional
from fastapi import FastAPI,status, HTTPException
from pydantic import BaseModel
from random import randrange

from starlette.responses import Response

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating: Optional[int] = None

my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},{"title":"best foods","content":"I like Pizza","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id']==id:
            return i

@app.get("/")
async def root():
    return{"message":"Hello World"}

@app.get("/posts")
async def get_posts():
    return{"data":my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id']= randrange(0,100000)
    my_posts.append(post_dict)
    return{"data":post_dict}

@app.get("/posts/{id}")
def get_post(id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    return{"post_deatil":post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    #deleting the post
    index= find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/post/{id}", status_code=status.)
def update_post(id:int):
