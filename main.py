from typing import ContextManager, Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating: Optional[int] = None

my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},{"title":"best foods","content":"I like Pizza","id":2}]

@app.get("/")
async def root():
    return{"message":"Hello World"}

@app.get("/posts")
async def get_post():
    return{"data":"This is a post"}


@app.post("/posts")
def create_post(post: Post):
    print(post)
    print(post.dict())
    return{"data":post}

##@app.post("/createposts")
##def create_post(payLoad:dict=Body(...)):
##   print(payLoad)
##   return {"new_post":f"title {payLoad['title']} Content:{payLoad['content']}"}