from pydantic import BaseModel
from typing import Optional



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
