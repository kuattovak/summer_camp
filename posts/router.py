from posts.schemas import CreatePostRequest
from posts.schemas import EditPostRequest
from fastapi import HTTPException, APIRouter

posts = {
    "photo":"kamila"
}
last_added_post_id = 1

router = APIRouter() 

@router.get('')
def get_posts():
    return posts
# function to get posts


@router.post('')
def create_post(post: CreatePostRequest):
    global last_added_post_id
    new_id = last_added_post_id + 1
    posts[new_id] = post
    last_added_post_id = new_id
    return new_id
# functions to create posts


@router.get('/{id}')
def get_post(id: int):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    return posts[id]
# function to get each post by id 


@router.put('/{id}')
def edit_post(id: int, post: EditPostRequest):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    for key, value in post.items():
        if value is not None:
            posts[id][key] = value

    return id
#  function to edit each post by id

@router.delete('/{id}')
def edit_post(id: int):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    del posts[id]

    return id
#  function to delete each post by id 
