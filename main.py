from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from posts.router import router
from database import database

# title
# content
# location
# author

app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()
    
@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

app.include_router(router, prefix = '/posts')



last_added_account_id = 1



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