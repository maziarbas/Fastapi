from typing import ContextManager, Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from fastapi import status

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

@app.get("/")
async def root():
    return{"message":"Hello World"}

@app.get("/posts")
async def get_posts():
    return{"data":my_posts}


@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id']= randrange(0,100000)
    my_posts.append(post_dict)
    return{"data":post_dict}

@app.get("/posts/{id}")
def get_post(id:int,response:Response):
    post = find_post(id)
    if not post:
        response.status_code= status.HTTP_404_NOT_FOUND
        return {"message":f"post with id {id} was not found"}
    return{"post_deatil":post}



##@app.post("/createposts")
##def create_post(payLoad:dict=Body(...)):
##   print(payLoad)
##   return {"new_post":f"title {payLoad['title']} Content:{payLoad['content']}"}