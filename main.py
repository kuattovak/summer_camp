from fastapi import FastAPI, HTTPException, Request
from typing import Dict, Optional
from pydantic import BaseModel

# title
# content
# location
# author

app = FastAPI()

posts = {
    "":""
}
last_added_post_id = -1
last_added_account_id = 1

class CreatePostRequest(BaseModel):
    title: str
    content: str
    author: str
    location: str
    # request form for creating post request

class EditPostRequest(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    location: Optional[str] = None
    # request form for editing post requests


@app.get('/posts')
def get_posts():
    return posts
# function to get posts


@app.post('/posts')
def create_post(post: CreatePostRequest):
    global last_added_post_id
    new_id = last_added_post_id + 1
    posts[new_id] = post
    last_added_post_id = new_id
    return new_id
# functions to create posts


@app.get('/post/{id}')
def get_post(id: int):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    return posts[id]
# function to get each post by id 


@app.put('/post/{id}')
def edit_post(id: int, post: EditPostRequest):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    for key, value in post.items():
        if value is not None:
            posts[id][key] = value

    return id
#  function to edit each post by id

@app.delete('/post/{id}')
def edit_post(id: int):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    del posts[id]

    return id
#  function to delete each post by id 

######################################
accounts = {
    0 : {
    "username":"kuattovak",
    "name":"Kamila",
    "surname":"Kuatova",
    "age":"16",
    "gender":"female"
    },
    1: {
    "username":"hansh_aiym",
    "name":"Khanshaiym",
    "surname":"Yegetayeva",
    "age":"16",
    "gender":"female"
    }
}

class UpdateUserRequest(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    age: Optional[str] = None
    gender: Optional[str] = None
    
class CreateUserRequest(BaseModel):
    username: str
    name: str
    surname: str 
    age: str
    gender: str
    


@app.get("/accounts")
def get_accounts():
    return accounts
    
@app.post("/accounts")
def create_post(post: CreateUserRequest):
    global last_added_account_id
    new_id = last_added_account_id + 1
    accounts[new_id] = post
    last_added_account_id = new_id
    return new_id
    
@app.get("/account/{id}")
def get_accountById(id:int):
    if id not in accounts:
        return HTTPException(status_code=404,detail=f'No account with id {id} was found')
    return accounts[id]
    
@app.put("/account/{id}")
def update_account(post: UpdateUserRequest,id: int):
    if id not in accounts:
        return HTTPException(status_code=404, detail= f'No account with id {id} was found')
    for key,value in accounts.items():
        if value is not None:
            accounts[id][key]=[value]
    return id

@app.delete("/account/{id}")
def delete_account(id: int):
    if id not in accounts:
        raise HTTPException(status_code=404, detail=f'No account with id {id} was found')
    
    del accounts[id]
    return id